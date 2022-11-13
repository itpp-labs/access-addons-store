/** @odoo-module **/
/*  Copyright 2022 Ivan Yelizariev <https://twitter.com/yelizariev>
    License OPL-1 (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#odoo-apps). */

import { localizationService } from "@web/core/l10n/localization_service";
import { translatedTerms } from "@web/core/l10n/translation";

const odoo_terms = [
    "Odoo Session Expired",
    "Your Odoo session expired. The current page is about to be refreshed.",
];

export const debrandTranslation = () => {
    if (!odoo.debranding_new_name) {
        return;
    }
    _.each(odoo_terms, (term) => {
        if (!translatedTerms[term]) {
            translatedTerms[term] = term;
        }
        translatedTerms[term] = term.replace(/Odoo/gi, odoo.debranding_new_name);
    });
};

const start = localizationService.start;
localizationService.start = async (env, { user }) => {
    await start(env, { user });
    debrandTranslation();
};
