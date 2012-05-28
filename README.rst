Introduction
--------------

This provides new view, *listless*, for Plone Folder content type.
It hides the folder listing in the content area, but still shows the folder title and the description.

Installation
------------

Add Dexterity to your buildout.cfg

* http://plone.org/products/dexterity/documentation/how-to/install

Then add listlessview egg in buildout.
In buildout.cfg::

        eggs =
                ...
                listlessview

Re-run buildout.

Usage
------

Install add-on.

Go to a folder.

Choose *Listless* from *Display* menu.

Author
------

`Mikko Ohtamaa <http://opensourcehacker.com>`_.

