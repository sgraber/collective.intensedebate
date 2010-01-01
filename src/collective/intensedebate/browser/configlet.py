from plone.app.controlpanel.form import ControlPanelForm
from zope.component import adapts
from zope.schema import TextLine, Bool, Int
from zope.formlib.form import Fields
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface, implements

from Products.CMFDefault.formlib.schema import ProxyFieldProperty, SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot

_ = MessageFactory('collective.intensedebate')


class IIntenseDebateSettings(Interface):
    """
    Defines configurable options of collective.intensedebate.
    """
    forum_id = TextLine(
        title = _(u"Your Intense Debate's 'idcomments_acct' string "),
        description = _(u"This string is used to uniquely identify your website for Intense Debate. It typically looks like 'f4e4d39dhdl756bcd98refbl321fl8ar'. Copy that string and paste it in the field below. You need to enter this ID before you begin using IntenseDebate on your website."),
        required = False
        )


class IntenseDebateControlPanel(ControlPanelForm):
    """
    Configlet for collective.intensedebate.
    """
    form_fields = Fields(IIntenseDebateSettings)
    label = _(u"Intense Debate Comment System")
    description = _("Fill out the below form fields with your IntenseDebate account information in order to activate it.")


class IntenseDebateControlPanelAdapter(SchemaAdapterBase):
    """
    Store values of IIntenseDebateConfiguration.
    """
    adapts(IPloneSiteRoot)
    implements(IIntenseDebateSettings)
    
    forum_id = ProxyFieldProperty(IIntenseDebateSettings['forum_id'])
    