/** @odoo-module **/
/*  Copyright 2016-2017 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
    Copyright 2017 ArtyomLosev <https://github.com/ArtyomLosev>
    Copyright 2022 IT-Projects <https://it-projects.info/>
    License OPL-1 (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#odoo-apps). */

import "@web_debranding/js/base";
import { _t } from "web.core";
import { patch } from "web.utils";
import { session } from "@web/session";

const web_session = session;
const components = {
    BusService: require("bus.BusService"),
};

patch(
    components.BusService.prototype,
    "web_debranding/static/src/js/native_notifications.js",
    {
        sendNotification(options, callback) {
            if (
                options.title === _t("Yay, push notifications are enabled!") ||
                options.title === _t("Permission denied")
            ) {
                options.message = options.message.replace(
                    /Odoo/gi,
                    odoo.debranding_new_name
                );
            }
            this._super(options, callback);
        },
        _sendNativeNotification: function (title, content, callback) {
            var notification = new Notification(
                // The native Notification API works with plain text and not HTML
                // unescaping is safe because done only at the **last** step
                _.unescape(title),
                {
                    body: _.unescape(content),
                    icon:
                        "/web/binary/company_logo?company_id=" + web_session.company_id,
                }
            );
            notification.onclick = function () {
                window.focus();
                if (this.cancel) {
                    this.cancel();
                } else if (this.close) {
                    this.close();
                }
                if (callback) {
                    return callback();
                }
            };
        },
    }
);
