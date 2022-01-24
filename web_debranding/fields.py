# -*- coding: utf-8 -*-
from openerp.fields import _String

get_trans_func = _String.get_trans_func


def get_trans_func_debrand(self, records):
    # check either web_debranding is installed
    if not hasattr(records.env['ir.translation'], '_debrand'):
        return get_trans_func(self, records)

    if True:  # keep original indent
        if callable(self.translate):
            rec_src_trans = records.env['ir.translation']._get_terms_translations(self, records)

            def translate(record_id, value):
                src_trans = rec_src_trans[record_id]

                def tr(source):
                    trans = src_trans.get(source, source)
                    return records.env['ir.translation']._debrand(trans)
                return self.translate(tr, value)

        else:
            rec_trans = records.env['ir.translation']._get_ids(
                '%s,%s' % (self.model_name, self.name), 'model', records.env.lang, records.ids)

            def translate(record_id, value):
                return rec_trans.get(record_id) or value

        return translate


_String.get_trans_func = get_trans_func_debrand
