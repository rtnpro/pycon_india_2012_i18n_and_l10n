Develop for an international audience
#####################################
:Speaker: Ratnadeep Debnath
:Event: Pycon 2012
:Slides: TODO

About me
--------
* Developer and QA at www.transifex.com
* rtnpro@{transifex|gmail}.com
* @rtnpro at Freenode, Twitter
* https://github.com/rtnpro
* http://ratnadeepdebnath.wordpress.com


Transifex
---------
* A modern localization workflow management system
* A Django based startup
* It's like a Github for localization
* Popular projects (among many) using Transifex:
  Fedora, Django, Dropbox, Pinterest, Opentranslators, Eventbrite, Intel, Nokia ...
* Code: https://github.com/transifex


i18n & l10n
-----------
* i18n: Internationalization
* l10n: Localization


Encoding
--------
* Always use Unicode rather than ASCII
* Decode user input
* Encode your application output


Timezone
--------
* Use UTC to save time information
* You can use **pytz** module for converting timezone info.


Choice of formats
-----------------
* Gettext
* Qt
* YAML
* INI

Use a real format
-----------------
* Plural support
* Context
* Comment
* Suggestions
* Validation

Basic steps for i18n and l10n
-----------------------------
* Mark translation strings
* Extract them (PO files)
* Translate them
* Compile them (MO files)
* Load them in application

Python & Gettext
----------------
.. code-block:: python

    from gettext import gettext as _

    string  = _(u'A sentence to translate')



i18n in Django models
---------------------
.. code-block:: python

    from django.utils.translation import ugettext_lazy as _

    class Person(models.Model):
        name = models.TextField(
            _('Name'),
            help_text=_('First & last name')
        )


i18n in Django templates
------------------------
.. code-block:: html

    {% load i18n %}

    {% trans "Person:" %}


Localize dynamic content
------------------------
* Add separate tables to hold localized data
* Add new fields in the same table to hold localized data
* Use Gettext to localize dynamic data


Gotchas with Gettext & Python
-----------------------------
* It's always better to use named format specifiers than positional format specifiers
* Are you using new Python format strings? Well, Gettext does not recognize
  them and so no validation support from it.


Challenges
----------
* Mark translate strings, export
* Release string freeze
* Translator: VCS checkout
* Translate w/ specialized tools
* Get 'em files back: SSH, email, tickets
* For every friggin release


Modern solutions
----------------
* Localization workflow management tools on the cloud

  - **Transifex**
  - **Gengo**
  - ...
* **Pontoon**: A tool from Mozilla for live website localization


Localization workflow management tools
--------------------------------------
* VCS abstraction
* Crowdsourced
* Agile
* API
* TM, Glossary


Pontoon
-------
* Live website localization
* Configurable with various backends like Transifex, Pootle, etc.
* Very intuitive
* Support for various web frameworks: **PHP**, **Django** (others will follow)
* Helps localize non i18n-ized websites
* Open Source


Contribute
----------
You can always contribute to Transifex and Pontoon.

They are open source :)


Questions?
----------

