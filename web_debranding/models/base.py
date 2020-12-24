# Copyright 2020 Ivan Yelizariev
# License OPL-1 (https://www.odoo.com/documentation/user/13.0/legal/licenses/licenses.html#odoo-apps).
from odoo import models

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
