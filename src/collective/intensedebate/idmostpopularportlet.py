from zope.interface import implements
from zope.i18nmessageid import MessageFactory

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

# custom additions below
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName

_ = MessageFactory('collective.intensedebate')


class IIDMostPopularPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IIDMostPopularPortlet)

    def __init__(self):
        pass

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return "ID Most Popular"


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """
    
    Title = 'Most Popular'
    render = ViewPageTemplateFile('idmostpopularportlet.pt')
    
    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

        context = aq_inner(self.context)

    def show(self):
        """Only render if we're viewing a Smart Folder and that the 
        current folder contains our cover image (cover.jpg) 
        OR we're in the portal root viewing a Topic.
        """
        return 

class AddForm(base.NullAddForm):
    """Portlet add form.
    """
    def create(self):
        return Assignment()

