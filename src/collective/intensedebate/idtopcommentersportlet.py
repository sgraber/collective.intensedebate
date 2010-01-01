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


# ----------------------------------------------------------------------------------------
# Thank you plone.portlet.collection for showing me how to implement all of this! 01/01/10
# ----------------------------------------------------------------------------------------


class IIDTopCommentersPortlet(IPortletDataProvider):
    """A portlet that displays the top commenters from Intense Debate.

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

    account_id = schema.Int(
        title = _(u"Your Intense Debate's Widget comments account number"),
        description = _(u"This number is used to uniquely identify your comments information from Intense Debate and it's different than your idcomments_acct number from above. You can find it within the Widgets section on Intense Debate's website.  It appears right after the /acctComments/ in the javascript that you'd copy to your blog go show a widget."),
        required = True
        )
        
    num_to_display = schema.Int(title = (u"Number of Intense Debate Comments to Display"),
                                description = (u"Enter the number of comments to display in the portlet when its rendered."
                            		" The portle defaults to '5', which is the same as the default on Intense Debate. "),
                                required = True,
                                default = 10)


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IIDTopCommentersPortlet)

    account_id = '' # the intense debate widget acct number
    num_to_display = 5 # number comments to initially display
    
    def __init__(self, account_id='', num_to_display=5):
        self.account_id = account_id
        self.num_to_display = num_to_display

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return "ID Top Commenters"


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """
    
    Title = 'Top Commenters'
    render = ViewPageTemplateFile('idtopcommentersportlet.pt')
    
    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        context = aq_inner(self.context)

    @property
    def account_id(self):
        """Get the Intense Debate Account ID from the Portal Configlet"""
        data = self.data
        account_id = data.account_id
        return str(account_id) # has to be a string!!!

    @property
    def num(self):
        """Number of comments to display"""
        data = self.data
        num = data.num_to_display 
        return str(num)  # has to be a string!!!


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IIDTopCommentersPortlet)
    
    label = _(u"Add Intense Debate Top Commenters Portlet")
    description = _(u"This portlet displays a listing of your top Intense Debate commenters.")
    
    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IIDTopCommentersPortlet)
    
    label = _(u"Edit Intense Debate Top Commenters Portlet")
    description = _(u"This portlet displays a listing of your top Intense Debate commenters.")
    