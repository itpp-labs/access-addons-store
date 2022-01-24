# Copyright 2015-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2017 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# Copyright 2018-2019 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# Copyright 2018 Ildar Nasyrov <https://it-projects.info/team/iledarn>
# Copyright 2018 WohthaN <https://github.com/WohthaN>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": "Backend debranding",
    "version": "11.0.1.0.28",
    "author": "IT-Projects LLC, Ivan Yelizariev",
    "license": "Other OSI approved licence",  # MIT
    "category": "Debranding",
    "images": ["images/web_debranding.png"],
    "website": "https://twitter.com/yelizariev",
    "price": 250.00,
    "currency": "EUR",
    "depends": ["web", "mail", "web_planner", "access_apps", "access_settings_menu"],
    "data": ["data.xml", "views.xml", "js.xml", "pre_install.yml"],
    "qweb": ["static/src/xml/web.xml"],
    "post_load": "post_load",
    "auto_install": False,
    "uninstall_hook": "uninstall_hook",
    "installable": True,
}
