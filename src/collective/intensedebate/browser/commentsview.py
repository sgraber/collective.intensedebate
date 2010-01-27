from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.intensedebate import intensedebateMessageFactory as _


class ItocView(Interface):
    """
    toc view interface
    """

    def test():
        """ test method"""


class tocView(BrowserView):
    """
    toc browser view
    """
    implements(ItocView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def test(self):
        """
        test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}
