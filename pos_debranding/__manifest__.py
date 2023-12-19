# Copyright 2015-2018,2020,2022-2023 Ivan Yelizariev <https://twitter.com/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": "POS debranding",
    "version": "17.0.1.0.0",
    "author": "IT-Projects LLC, Ivan Yelizariev",
    "license": "Other OSI approved licence",  # MIT
    "category": "Debranding",
    "support": "help@itpp.dev",
    "website": "https://odoo-debranding.com",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale.assets_prod": [
            "pos_debranding/static/src/xml/pos_debranding.xml",
        ],
        "web.assets_tests": [
            "pos_debranding/static/src/js/tour.js",
        ],
    },
    "data": [
        "views/pos.xml",
    ],
    "installable": True,
}
