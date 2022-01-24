# -*- coding: utf-8 -*-
from openerp import models, api
from openerp.tools.translate import _

PARAMS = [
    ('web_debranding.new_name', _('Software')),
    ('web_debranding.new_title', _('Software')),
    ('web_debranding.new_website', 'example.com'),
    ('web_debranding.favicon_url', ''),
    ('web_debranding.send_publisher_warranty_url', '0'),
    ('web_debranding.planner_footer', ''),
]


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def get_debranding_parameters(self):
        res = {}
        for param, default in PARAMS:
            value = self.env['ir.config_parameter'].get_param(param, default)
            res[param] = value.strip()
        return res

    @api.model
    def create_debranding_parameters(self):
        for param, default in PARAMS:
            self.env['ir.config_parameter'].set_param(param, default or ' ')
