"""

    Plone views overrides.

    For more information see

    * http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

"""

# Disable unused imports pylint warning as they are here
# here for example purposes
# W0611: 12,0: Unused import Interface

# pylint: disable=W0611

# Zope imports
from five import grok
from Products.CMFCore.interfaces import IFolderish

# Local imports
from interfaces import IAddonSpecific

grok.templatedir("templates")
grok.layer(IAddonSpecific)


class ListlessView(grok.View):
    """
    Render a folder title + description only.
    """

    grok.name("listless")
    grok.template("listless")
    grok.context(IFolderish)
