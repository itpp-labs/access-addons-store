/** @odoo-module **/
/*  Copyright 2016-2017 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
    Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
    License MIT (https://opensource.org/licenses/MIT).
    Copyright 2022 IT-Projects <https://it-projects.info/>
    License OPL-1 (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#odoo-apps). */

import "@web_debranding/js/dialog";

// FIXME: require is not defined
const components = {
    Message: require("@mail/components/message/message"),
    ThreadPreview: require("@mail/components/thread_preview/thread_preview"),
};

const session = require("web.session");
const { patch } = require("web.utils");

patch(components.ThreadPreview, "web_debranding/static/src/js/bot.js", {
    image() {
        if (
            this.thread.correspondent &&
            this.thread.correspondent === this.env.messaging.partnerRoot
        ) {
            return "/web/binary/company_logo?company_id=" + session.company_id;
        }
        return this._super();
    },
});

patch(components.Message, "web_debranding/static/src/js/message.js", {
    avatar_debranded() {
        if (
            this.message.author &&
            this.message.author === this.env.messaging.partnerRoot
        ) {
            return "/web/binary/company_logo?company_id=" + session.company_id;
        }

        return this.avatar;
    },
});
