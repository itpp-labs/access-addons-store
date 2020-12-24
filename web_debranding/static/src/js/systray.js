/*  Copyright 2020 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
    License MIT (https://opensource.org/licenses/MIT). */
odoo.define('web_debranding.systray', function (require) {
    "use strict";
    var SystrayMenu = require('web.SystrayMenu');

    SystrayMenu.include({

        willStart: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function (res) {
                console.log(self);
                _.each(self.widgets, function(w){
                    var $gift = w.$el.find('.gift_icon');
                    if($gift && $gift.length) {
                        $gift.off();
                        $gift[0].href = odoo.debranding_new_website;
                    }
                });
                return res;
            });
        },
    });

});
