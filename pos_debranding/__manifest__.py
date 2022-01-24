{
    "name": "POS debranding",
    "version": "12.0.1.0.0",
    "author": "IT-Projects LLC, Ivan Yelizariev",
    "license": "Other OSI approved licence",  # MIT
    "category": "Debranding",
    "support": "apps@itpp.dev",
    "website": "https://www.odoo.com/apps/modules/12.0/pos_debranding/",
    "depends": ["point_of_sale"],
    # 'price': 30.00,
    # 'currency': 'EUR',
    "data": ["views.xml", "template.xml"],
    "qweb": ["static/src/xml/pos_debranding.xml"],
    "installable": True,
}
