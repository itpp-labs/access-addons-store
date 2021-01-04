====================
 Backend debranding
====================

Installation
============

* `Install <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__ this module in a usual way

Configuration
=============

By default the module replaces ``Odoo`` to ``Software``.

* Switch to Developer mode
* Open ``[[ General Settings ]] >> Technical >> Parameters >> System Parameters`` and modify:

  * ``web_debranding.new_title`` (put space in *Value field* if you don't need Brand in Title)
  * ``web_debranding.new_name`` (your Brand)
  * ``web_debranding.new_website`` (your website)
  * ``web_debranding.new_documentation_website`` (website with documentation instead of official one)
  * ``web_debranding.favicon_url``
  * ``web_debranding.send_publisher_warranty_url`` - set 0 to disable server requests to odoo.com and 1 otherwise (useful for enterprise contractors). Works only for non-enterprise versions of odoo, check `note <https://www.odoo.com/apps/modules/14.0/web_debranding/#enterprise-users-notice>`__ below.
  * ``web_debranding.icon_url`` - icon for mobile devices *recommended size :192x192*
  * ``web_debranding.apple_touch_icon_url`` - icon for IOS Safari *recommended size :152x152*

Further debranding
==================

* Open *addons/mail/data/mail_data.xml* and edit Template **Notification Email** - delete ``using Odoo``
* Install `website_debranding <https://apps.odoo.com/apps/modules/14.0/website_debranding/>`__ if module *Website Builder* has been already installed in your system
* Install `pos_debranding <https://apps.odoo.com/apps/modules/14.0/pos_debranding/>`__ if module `POS` has been already installed in your system
* Delete *Odoo.com Accounts* record at *Settings >> Users & Companies >> OAuth Providers* if module ``OAuth2 Authentication`` has been already installed in your system
* To debrand ``/web/database/manager``:

  * Either set `list_db <https://www.odoo.com/documentation/14.0/setup/deploy.html#database-manager-security>`__ to value ``False``

  * or edit *addons/web/views/database_manager.html* file:

    * delete or modify **<title>** tag
    * delete or modify favicon
    * delete or modify **<img>** tag with ``logo2.png``
    * delete or modify warning **<div class="alert alert-warning"> Warning, your Odoo database ...</div>**
    * delete or modify **<small class="text-muted">** To enhance your experience, some data may be sent to *Odoo online services*. See our `Privacy Policy <https://www.odoo.com/privacy>`__
    * delete or modify **<p class="form-text"> In order to avoid conflicts between databases, Odoo needs ...</p>**

* Delete following modules and remove ``'auto_install': True,`` attribute from their ``__manifest__.py`` files:

  * ``iap`` (*In-App Purchases*)
  * ``odoo_refferal`` (*Odoo referral program*)
* Favicon

  * in existing database, you may need to open ``[[ Settings ]] >> Users & Companies >> Companies`` and change **Company Favicon**
  * for new companies odoo default favicon is empty
  * to get debranded favicon in new datatabase check next section

Auto-debrand new databases
==========================

To automatically install this module for every new databases set 'auto_install': True in ``__manifest__.py`` files of following modules:

* ``web_debranding``
* ``ir_rule_protected``
* ``access_restricted``
* ``access_apps``
* ``access_settings_menu``
* ``mail (built-in)``
* ``base_setup (built-in)``
* ``bus (built-in)``

Also, it's recommended to add ``web_debranding`` to `server wide modules <https://odoo-development.readthedocs.io/en/latest/admin/server_wide_modules.html>`__, e.g.::

    ./odoo-bin --load=base,web,web_debranding
Usage
=====
* Open *Backend*
* Perform usual workflow

RESULT: No more reference to `Odoo <https://www.odoo.com/>`__. *Possible exceptions may be Mails.*

Examples
========

* Search a random string at the menu ``[[ Settings ]] >> Users & Companies >> Companies``

    Create and manage the companies that will be managed by **Odoo** from here. Shops or subsidiaries can be created and maintained from here.

* Try to delete Administrator via menu ``[[ Settings ]] >> Users & Copanies >> Users``

    You can not remove the admin user as it is used internally for resources created by *Odoo** (updates, module installation, ...).

  Note: You may see another error depending on installed modules.

* When you create new company it shows placeholder for field **Website**

    e.g. www.odoo.com

* Open menu ``[[ Settings ]] >> General Settings``.

    Use external pads in **Odoo** Notes.

    Extract and analyze **Odoo** data from Google Spreadsheet.

* Open menu ``[[ Discuss ]] >> CHANNELS >> #general``

  * Send ``/help`` to the chat

    **OdooBot** - now

    You are in channel #general.

    You can mention someone by typing @username, this will grab its attention.

    You can mention a channel by typing #channel.

    You can execute a command by typing /command.

    You can insert canned responses in your message by typing :shortcut.
