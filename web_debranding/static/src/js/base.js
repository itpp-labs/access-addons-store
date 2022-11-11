/** @odoo-module **/
/*  Copyright 2015-2018,2022 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
    Copyright 2017 ArtyomLosev <https://github.com/ArtyomLosev>
    Copyright 2022 IT-Projects <https://it-projects.info/>
    License MIT (https://opensource.org/licenses/MIT). */

import { WebClient } from "@web/webclient/webclient";
import { patch } from "web.utils";
const { onMounted } = owl.hooks;
import { useService } from "@web/core/utils/hooks";

const components = { WebClient };

patch(components.WebClient.prototype, "web_debranding/static/src/js/base.js", {
    setup() {
        this._super();
        odoo.debranding_new_name = "";
        odoo.debranding_new_website = "";
        odoo.debranding_new_title = "";
        this.title.setParts({ zopenerp: odoo.debranding_new_title });
        this.orm = useService("orm");
        onMounted(() => {
            this.updateDebrandingValues();
        });
    },
    async updateDebrandingValues() {
        const result = await this.orm.call(
            "ir.config_parameter",
            "get_debranding_parameters"
        );
        odoo.debranding_new_name = result["web_debranding.new_name"];
        odoo.debranding_new_website = result["web_debranding.new_website"];
        odoo.debranding_new_title = result["web_debranding.new_title"];
        this.title.setParts({ zopenerp: odoo.debranding_new_title });
    },
});
