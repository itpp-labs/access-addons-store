# Copyright 2024 Ivan Yelizariev <https://twitter.com/yelizariev>
# License OPL-1 (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#odoo-apps)
{
    "name": "Relaxation Room",
    "version": "16.0.1.0.0",
    "author": "Ivan Yelizariev",
    "license": "OPL-1",
    "category": "Human Resources",
    "images": ["images/oobo7.jpg"],
    "website": "https://odoo-debranding.com",
    "support": "help@itpp.dev",
    "depends": [],
    "data": [
        "views/relax_views.xml",
        "data/relax_data.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "relax/static/src/js/relax.js",
            "relax/static/src/xml/relax.xml",
            "relax/static/src/scss/relax.scss",
        ]
    },
    "application": True,
    "auto_install": False,
    "installable": True,
}
