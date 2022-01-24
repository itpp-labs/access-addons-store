# -*- coding: utf-8 -*-
import logging

from odoo import api, models
from odoo.tools import mute_logger

from .ir_translation import debrand

_logger = logging.getLogger(__name__)

MODULE = "_web_debranding"


class View(models.Model):
    _inherit = "ir.ui.view"

    @api.multi
    def read_combined(self, fields=None):
        res = super(View, self).read_combined(fields=fields)
        if isinstance(res["arch"], str) and not isinstance(res["arch"], unicode):
            res["arch"] = res["arch"].decode("utf-8")
        res["arch"] = debrand(self.env, res["arch"])
        return res

    @api.model
    def _create_debranding_views(self):

        self._create_view(
            "menu_secondary",
            "web.menu_secondary",
            """
        <xpath expr="//div[@class='o_sub_menu_footer']" position="replace">
           <div class="o_sub_menu_footer"></div>
       </xpath>""",
        )

        self._create_view(
            "webclient_bootstrap_enterprise_title",
            "web.webclient_bootstrap",
            """
       <xpath expr="//title" position="replace"></xpath>""",
        )

        self._create_view(
            "webclient_bootstrap_enterprise_favicon",
            "web.webclient_bootstrap",
            """
       <xpath expr="//link[@rel='shortcut icon']" position="replace">
           <t t-set="favicon" t-value="request and request.env['ir.config_parameter'].get_debranding_parameters().get('web_debranding.favicon_url', '')"/>
           <t t-if="favicon">
               <link rel="shortcut icon" t-att-href="favicon" type="image/x-icon"/>
           </t>
       </xpath>""",
        )

        self._create_view(
            "webclient_bootstrap_enterprise_mobile_icon",
            "web.webclient_bootstrap",
            """
        <xpath expr="//link[@rel='icon']" position="replace">
            <t t-set="icon" t-value="request and request.env['ir.config_parameter'].get_debranding_parameters().get('web_debranding.icon_url', '')"/>
            <t t-if="icon">
                <link rel="icon" sizes="192x192" t-att-href="icon" type="image/x-icon"/>
            </t>
        </xpath>""",
        )

        self._create_view(
            "webclient_bootstrap_enterprise_apple_touch_icon",
            "web.webclient_bootstrap",
            """
        <xpath expr="//link[@rel='apple-touch-icon']" position="replace">
            <t t-set="icon" t-value="request and request.env['ir.config_parameter'].get_debranding_parameters().get('web_debranding.apple_touch_icon_url', '')"/>
            <t t-if="icon">
                <link rel="apple-touch-icon" t-att-href="icon" type="image/x-icon"/>
            </t>
        </xpath>""",
        )

    @api.model
    def _create_view(self, name, inherit_id, arch, noupdate=False, view_type="qweb"):
        view = self.env.ref("{}.{}".format(MODULE, name), raise_if_not_found=False)
        if view:
            try:
                view.write({"arch": arch})
                view._check_xml()
            except Exception:
                _logger.warning(
                    "Cannot update view %s. Delete it.", name, exc_info=True
                )
                view.unlink()
                return

            return view.id

        try:
            with self.env.cr.savepoint(), mute_logger("odoo.models"):
                view = self.env["ir.ui.view"].create(
                    {
                        "name": name,
                        "type": view_type,
                        "arch": arch,
                        "inherit_id": self.env.ref(
                            inherit_id, raise_if_not_found=True
                        ).id,
                    }
                )
                view._check_xml()
        except Exception:
            _logger.debug("Cannot create view %s. Cancel.", name, exc_info=True)
            return
        self.env["ir.model.data"].create(
            {
                "name": name,
                "model": "ir.ui.view",
                "module": MODULE,
                "res_id": view.id,
                "noupdate": noupdate,
            }
        )
        return view.id
