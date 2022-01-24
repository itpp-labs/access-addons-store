# -*- coding: utf-8 -*-
import re

from odoo import api, models, tools

from .ir_config_parameter import PARAMS


def debrand_documentation_links(source, new_documentation_website):
    return re.sub(
        r"https://www.odoo.com/documentation/",
        new_documentation_website + u"documentation/",
        source,
        flags=re.IGNORECASE,
    )


def debrand_links(source, new_website):
    return re.sub(r"\bodoo.com\b", new_website, source, flags=re.IGNORECASE)


def debrand(env, source):
    if isinstance(source, str) and not isinstance(source, unicode):
        source = source.decode("utf-8")
    if not source or not re.search(r"\bodoo\b", source, re.IGNORECASE):
        return source

    if env:
        params = env["ir.config_parameter"].get_debranding_parameters()
    else:
        # use default values
        params = dict(PARAMS)

    new_name = params.get("web_debranding.new_name")
    new_website = params.get("web_debranding.new_website")
    new_documentation_website = params.get("web_debranding.new_documentation_website")

    source = debrand_documentation_links(source, new_documentation_website)
    source = debrand_links(source, new_website)
    # We must exclude the next cases, which occur only in a code,
    # Since JS functions are also contained in the localization files.
    # Next regular expression exclude from substitution 'odoo.SMTH', 'odoo =', 'odoo=', 'odooSMTH', 'odoo['
    # Where SMTH is an any symbol or number or '_'. Option odoo.com were excluded previously.
    # Examples:
    # odoo.
    # xml file: https://github.com/odoo/odoo/blob/9.0/addons/im_livechat/views/im_livechat_channel_templates.xml#L148
    # odooSMTH
    # https://github.com/odoo/odoo/blob/11.0/addons/website_google_map/views/google_map_templates.xml#L14
    # odoo =
    # https://github.com/odoo/odoo/blob/11.0/addons/web/views/webclient_templates.xml#L260
    # odoo[
    # https://github.com/odoo/odoo/blob/11.0/addons/web_editor/views/iframe.xml#L43-L44
    source = re.sub(
        r"\bodoo(?!\.\S|\s?=|\w|\[)\b", new_name, source, flags=re.IGNORECASE
    )

    return source


class IrTranslation(models.Model):
    _inherit = "ir.translation"

    @api.model
    def _debrand_dict(self, res):
        for k in res:
            res[k] = self._debrand(res[k])
        return res

    @api.model
    def _debrand(self, source):
        return debrand(self.env, source)

    @tools.ormcache("name", "types", "lang", "source", "res_id")
    def __get_source(self, name, types, lang, source, res_id):
        res = super(IrTranslation, self).__get_source(name, types, lang, source, res_id)
        return self._debrand(res)

    @api.model
    @tools.ormcache_context("model_name", keys=("lang",))
    def get_field_string(self, model_name):
        res = super(IrTranslation, self).get_field_string(model_name)
        return self._debrand_dict(res)

    @api.model
    @tools.ormcache_context("model_name", keys=("lang",))
    def get_field_help(self, model_name):
        res = super(IrTranslation, self).get_field_help(model_name)
        return self._debrand_dict(res)
