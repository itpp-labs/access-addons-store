/** @odoo-module **/
// Copyright 2015-2018,2020,2022-2023 Ivan Yelizariev <https://twitter.com/yelizariev>
// License OPL-1 (https://www.odoo.com/documentation/17.0/legal/licenses.html#odoo-apps)
import { registry } from "@web/core/registry";
import { stepUtils } from "@web_tour/tour_service/tour_utils";

registry.category("web_tour.tours").add("pos_debranding.tour", {
    url: "/web",
    steps: () => [
        stepUtils.showAppsMenuItem(),
        {
            test: true,
            trigger: '.o_app[data-menu-xmlid="point_of_sale.menu_point_root"]',
            content: "Ready to launch your <b>point of sale</b>? <i>Click here</i>.",
            position: "right",
            edition: "community",
        },
        {
            trigger: '.o_app[data-menu-xmlid="point_of_sale.menu_point_root"]',
            content: "Ready to launch your <b>point of sale</b>? <i>Click here</i>.",
            position: "bottom",
            edition: "enterprise",
        },
        {
            trigger: ".o_pos_kanban button.oe_kanban_action_button",
            content:
                "<p>Click to start the point of sale interface. It <b>runs on tablets</b>, laptops, or industrial hardware.</p><p>Once the session launched, the system continues to run without an internet connection.</p>",
            position: "bottom",
        },
        {
            trigger: ".pos-content",
            content: "waiting for loading to finish",
            timeout: 20000,
            run: function () {
                // It's a check
            },
        },
        {
            content: "Switch to table or make dummy action",
            trigger: ".table:not(.oe_invisible .neworder-button), .pos-logo",
            position: "bottom",
        },
        {
            trigger:
                ".pos-branding:not(:has(>.pos-logo[src='/point_of_sale/static/src/img/logo.png']))",
            content: "Check logo",
            run: function () {
                // It's a check
            },
        },
    ],
});
