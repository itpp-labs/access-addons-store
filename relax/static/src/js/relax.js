/** @odoo-module **/
import { registry } from "@web/core/registry";
import rpc from "web.rpc";

const { Component, onWillStart } = owl;

export class RelaxMenu extends Component {
    setup() {
        this.config = rpc.query({
            model: "ir.config_parameter",
            method: "get_param",
            args: ["relax.url"],
        });

        onWillStart(async () => {
            this.relax_url = await this.config;
        });
    }
}

RelaxMenu.template = "relax.template";

registry.category("actions").add("relax", RelaxMenu);
