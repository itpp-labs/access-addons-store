# Copyright 2015-2018,2020 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2016 Stanislav Krotov <https://it-projects.info/team/ufaks>
# Copyright 2017 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# Copyright 2017 Nicolas JEUDY <https://github.com/njeudy>
# Copyright 2017 Ildar Nasyrov <https://it-projects.info/team/iledarn>
# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License MIT (https://opensource.org/licenses/MIT).
# License OPL-1 (https://www.odoo.com/documentation/user/13.0/legal/licenses/licenses.html#odoo-apps) for derivative work.

import base64
import functools
import io

import odoo
from odoo import http
from odoo.http import request
from odoo.modules import get_module_resource

from odoo.addons.web.controllers.main import Binary, WebClient

from ..models.ir_translation import debrand_bytes

db_monodb = http.db_monodb


class BinaryCustom(Binary):
    @http.route(
        ["/web/binary/company_logo", "/logo", "/logo.png"], type="http", auth="none"
    )
    def company_logo(self, dbname=None, **kw):
        imgname = "logo.png"
        default_logo_module = "web_debranding"
        if request.session.db:
            default_logo_module = (
                request.env["ir.config_parameter"]
                .sudo()
                .get_param("web_debranding.default_logo_module")
            )
        placeholder = functools.partial(
            get_module_resource, default_logo_module, "static", "src", "img"
        )
        uid = None
        if request.session.db:
            dbname = request.session.db
            uid = request.session.uid
        elif dbname is None:
            dbname = db_monodb()

        if not uid:
            uid = odoo.SUPERUSER_ID

        if not dbname:
            response = http.send_file(placeholder(imgname))
        else:
            try:
                # create an empty registry
                registry = odoo.modules.registry.Registry(dbname)
                with registry.cursor() as cr:
                    cr.execute(
                        """SELECT c.logo_web, c.write_date
                                    FROM res_users u
                               LEFT JOIN res_company c
                                      ON c.id = u.company_id
                                   WHERE u.id = %s
                               """,
                        (uid,),
                    )
                    row = cr.fetchone()
                    if row and row[0]:
                        image_data = io.BytesIO(base64.b64decode(row[0]))
                        response = http.send_file(
                            image_data, filename=imgname, mtime=row[1]
                        )
                    else:
                        response = http.send_file(placeholder("nologo.png"))
            except Exception:
                response = http.send_file(placeholder(imgname))
        return response


class WebClientCustom(WebClient):
    @http.route()
    def qweb(self, *args, **kwargs):
        response = super(WebClientCustom, self).qweb(*args, **kwargs)
        data = response.get_data()
        data = debrand_bytes(request.session.db and request.env or None, data)
        response.set_data(data)
        return response
