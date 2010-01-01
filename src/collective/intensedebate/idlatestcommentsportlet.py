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
from collective.intensedebate.browser.configlet import IIntenseDebateSettings


_ = MessageFactory('collective.intensedebate')


# ----------------------------------------------------------------------------------------
# Thank you plone.portlet.collection for showing me how to implement all of this! 01/01/10
# ----------------------------------------------------------------------------------------


class IIDLatestCommentsPortlet(IPortletDataProvider):
    """A portlet that displays the latest comments from Intense Debate.

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """
    # TODO: Add any zope.schema fields here to capture portlet configuration
    # information. Alternatively, if there are no settings, leave this as an
    # empty interface - see also notes around the add form and edit form
    # below.

    # some_field = schema.TextLine(title=_(u"Some field"),
    #                              description=_(u"A field to use"),
    #                              required=True)

    num_to_display = schema.Int(title = (u"Number of Intense Debate Comments to Display"),
                               description = (u"Enter the number of comments to display in the portlet when its rendered. "
                            		"The portle defaults to '5', which is the same as the default on Intense Debate. "),
                                required = True,
                                default = 5)

class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """
    
    implements(IIDLatestCommentsPortlet)
    
    num_to_display = 5 # number comments to initially display
    
    def __init__(self, num_to_display=5):
        self.num_to_display = num_to_display

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return "ID Latest Comments"


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """
    
    Title = 'Latest Comments'
    render = ViewPageTemplateFile('idlatestcommentsportlet.pt')
	
    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        context = aq_inner(self.context)

    def account_id(self):
        """Get the Intense Debate Account ID from the Portal Configlet"""
        portal_url = getToolByName(self.context, 'portal_url')
        portal = portal_url.getPortalObject()
        self.settings = IIntenseDebateSettings(portal)
        account_id = self.settings.account_id
        return account_id

    def num(self):
        """Number of comments to display"""
        num = self.num_to_display # for some reason this is returning an AttributeError
        return str(num)  # has to be a string!!!
        # Module collective.intensedebate.idlatestcommentsportlet, line 95, in num AttributeError: num_to_display

class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IIDLatestCommentsPortlet)
    
    label = _(u"Add Intense Debate Latest Comments Portlet")
    description = _(u"This portlet displays a listing of your latest Intense Debate comments.")
    
    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IIDLatestCommentsPortlet)
    
    label = _(u"Edit Intense Debate Latest Comments Portlet")
    description = _(u"This portlet displays a listing of your latest Intense Debate comments.")
    