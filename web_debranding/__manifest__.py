# Copyright 2015-2020 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2017 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# Copyright 2018-2019 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# Copyright 2018 Ildar Nasyrov <https://it-projects.info/team/iledarn>
# Copyright 2018 WohthaN <https://github.com/WohthaN>
# Copyright 2019-2020 Eugene Molotov <https://github.com/em230418>
# Copyright 2020 Denis Mudarisov <https://github.com/trojikman>
# License MIT (https://opensource.org/licenses/MIT).
# License OPL-1 (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#odoo-apps) for derivative work.
{
    "name": "Backend debranding",
    "version": "14.0.1.0.32",
    "author": "IT-Projects LLC, Ivan Yelizariev",
    "license": "OPL-1",
    "category": "Debranding",
    "images": ["images/web_debranding.png"],
    "website": "https://odoo-debranding.com",
    "support": "apps@itpp.dev",
    "price": 300.00,
    "currency": "EUR",
    "depends": ["base_setup", "web", "mail", "access_settings_menu", "mail_bot"],
    "data": [
        "data.xml",
        "views.xml",
        "js.xml",
        "pre_install.xml",
        "views/res_config.xml",
    ],
    "qweb": [
        "static/src/xml/bot.xml",
        "static/src/xml/web.xml",
    ],
    "post_load": "post_load",
    "auto_install": False,
    "uninstall_hook": "uninstall_hook",
    "installable": True,
    "saas_demo_title": "Backend debranding demo",
}
