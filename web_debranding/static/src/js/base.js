/** @odoo-module **/
/*  Copyright 2015-2018,2022 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
    Copyright 2017 ArtyomLosev <https://github.com/ArtyomLosev>
    Copyright 2022 IT-Projects <https://it-projects.info/>
    License MIT (https://opensource.org/licenses/MIT). */

import { WebClient } from "@web/webclient/webclient";
import { patch } from "web.utils";

const components = { WebClient };
// FIXME
const rpc = require("web.rpc");

patch(components.WebClient.prototype, "web_debranding/static/src/js/base.js", {
    setup() {
        this._super();
        odoo.debranding_new_name = "";
        odoo.debranding_new_website = "";
        odoo.debranding_new_title = "";
        this.title.setParts({ zopenerp: odoo.debranding_new_title });

        rpc.query(
            {
                model: "ir.config_parameter",
                method: "get_debranding_parameters",
            },
            {
                shadow: true,
            }
        ).then((result) => {
            odoo.debranding_new_name = result["web_debranding.new_name"];
            odoo.debranding_new_website = result["web_debranding.new_website"];
            odoo.debranding_new_title = result["web_debranding.new_title"];
            this.title.setParts({ zopenerp: odoo.debranding_new_title });
        });
    },
});
