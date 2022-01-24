# Copyright 2020 Ivan Yelizariev
# License OPL-1 (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#odoo-apps).
from odoo import api, models

from .ir_translation import debrand

BRANDED_FIELDS = {
    "mail.template": ["body_html", "name"],
    "mailing.mailing": ["body_html"],
}


class Base(models.AbstractModel):

    _inherit = "base"

    def _read(self, fields):
        super(Base, self)._read(fields)
        if self._name not in BRANDED_FIELDS.keys():
            return

        for f in BRANDED_FIELDS[self._name]:
            values = []
            for r in self:
                values.append(debrand(self.env, r[f]))
            field = self._fields[f]
            self.env.cache.update(self, field, values)

    @api.model
    def search(self, domain, offset=0, limit=None, order=None, count=False):
        res = super().search(domain, offset, limit, order, count)
        if self._name == "payment.acquirer":
            res = res.filtered(lambda a: not a.module_to_buy)
        return res
