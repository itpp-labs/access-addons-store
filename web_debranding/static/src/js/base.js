/** @odoo-module **/
/*  Copyright 2015-2018,2022 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
    Copyright 2017 ArtyomLosev <https://github.com/ArtyomLosev>
    License MIT (https://opensource.org/licenses/MIT). */
import { WebClient } from "@web/webclient/webclient";

export class WebClientDebranded extends WebClient {
    setup() {
        const self = this;
        super.setup(...arguments);
        this.title.setParts({ zopenerp: "" });
        odoo.debranding_new_name = "";
        odoo.debranding_new_website = "";
        odoo.debranding_new_title = "";

        this.rpc(
            {
                model: "ir.config_parameter",
                method: "get_debranding_parameters",
            },
            {
                shadow: true,
            }
        ).then(function (result) {
            odoo.debranding_new_name = result["web_debranding.new_name"];
            odoo.debranding_new_website = result["web_debranding.new_website"];
            odoo.debranding_new_title = result["web_debranding.new_title"];
            this.title.setParts({zopenerp: odoo.debranding_new_title});
        });
    }
}
