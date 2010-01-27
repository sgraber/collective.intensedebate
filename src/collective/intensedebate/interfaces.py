from zope.interface import implements, Interface
from zope.i18nmessageid import MessageFactory

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


_ = MessageFactory('collective.intensedebate')

class IIDCommentsView(Interface):
    """
    toc view interface
    """


class IDCommentsView(BrowserView):
    """
    toc browser view
    """
    implements(IIDCommentsView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

