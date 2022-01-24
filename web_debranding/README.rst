Backend debranding
==================

Removes references to odoo.com:

1. Deletes Odoo label in footer
2. Replaces "Odoo" in page title
3. Replaces "Odoo" in help message for empty list
4. Deletes Odoo link (as well as "Manage databases" link) from login page
5. Deletes About Odoo link
6. Replaces default logo by empty image
7. Replaces "Odoo" in Dialog Box
8. Replaces "Odoo" in strings marked for translation.
9. Replaces default favicon to a custom one
10. **Hides Modules menu** (by default, only admin user see Modules menu. You could change it via tick "Show Modules Menu" in user's access rights tab)
11. Removes odoo.com bindings (via disable_openerp_online module)
12. Deletes "Sent by ... using OpenERP" footer in email (via mail_delete_sent_by_footer module)

By default the module replaces "Odoo" to "Software". To configure
module open Settings\\System Parameters and modify

* web_debranding.new_title (put space in value if you don't need Brand in Title)
* web_debranding.new_name
* web_debranding.favicon_url

Further debranding
==================

* install **website_debranding** module if module "Website Builder" is installed in your system
* uninstall im_odoo_support module.
* delete "Odoo.com Accounts" record at Settings\\Users\\OAuth Providers if module "OAuth2 Authentication" is installed. in your system
* to debrand **/web/database/manager**:

  * add web_debranding to server wide modules, e.g.

	./odoo.py --load=web,web_kanban,web_debranding

  * edit addons/web/views/database_manager.html file:

    * delete or modify <title> tag
    * delete or modify favicon
    * right after script tag with src="/web/static/src/js/boot.js" add code below:
    
          <!-- debranding -->
    
          <script type="text/javascript" src="/web_debranding/static/src/js/main.js"></script>
    
          <script type="text/javascript" src="/web_debranding/static/src/js/title.js"></script>
    
          <script type="text/javascript" src="/web_debranding/static/src/js/about.js"></script>
    
          <script type="text/javascript" src="/web_debranding/static/src/js/dialog.js"></script>
    
          <link href="/web_debranding/static/src/css/database_manager.css" rel="stylesheet"/>

  

Tested on Odoo 8.0 eeedd2d9f52d46d8193059854e7430ca0c1fd6c0
