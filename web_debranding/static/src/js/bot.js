/** @odoo-module **/
/*  Copyright 2016-2017,2022 Ivan Yelizariev <https://twitter.com/yelizariev>
    Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
    Copyright 2022 IT-Projects <https://it-projects.info/>
    License OPL-1 (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#odoo-apps). */

import "@web_debranding/js/dialog";
import { Message } from "@mail/components/message/message";
import { patch } from "web.utils";
import { ThreadPreview } from "@mail/components/thread_preview/thread_preview";
import session from "web.session";

const components = { Message, ThreadPreview };

patch(components.ThreadPreview.prototype, "web_debranding/static/src/js/bot.js", {
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

patch(components.Message.prototype, "web_debranding/static/src/js/message.js", {
    avatar_debranded() {
        if (
            this.messageView.message.author &&
            this.messageView.message.author === this.messaging.partnerRoot
        ) {
            return "/web/binary/company_logo?company_id=" + session.company_id;
        }

        return this.avatar;
    },
});
