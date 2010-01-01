from zope.component import getUtility
from zope.component import getMultiAdapter
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from Products.CMFCore.utils import getToolByName

    
def install(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-collective.intensedebate:default')
    return "Ran all import steps."


def uninstall(portal):
    'Uninstall portal_controlpanel configlet'
    
    out = []
    cp = getToolByName(portal, 'portal_controlpanel', None)
    setup_tool = getToolByName(portal, 'portal_setup')

    # Remove import steps
    setup_tool.runAllImportStepsFromProfile('profile-collective.intensedebate:uninstall')
    out.append('Ran runAllImportStepsFromProfile.')

    # Remove the configlet from the portal control panel:
    if cp:
        if "IntenseDebateConfig" in [ c.id for c in cp._actions ]:
            cp.unregisterConfiglet("IntenseDebateConfig")
            out.append('Removed configlet for IntenseDebateConfig')

    # Remove installed portlets from columns
    id_portlets = ('id-latest-comments',
                   'id-most-popular',
                   'id-top-commenters',
                   )
                   
    rightcol = getUtility(IPortletManager, name=u'plone.rightcolumn', context=portal)
    right = getMultiAdapter((portal, rightcol,), IPortletAssignmentMapping, context=portal)
    leftcol = getUtility(IPortletManager, name=u'plone.leftcolumn', context=portal)
    left = getMultiAdapter((portal, leftcol,), IPortletAssignmentMapping, context=portal)
    
    for portlet in id_portlets:
        if portlet in right:
            del right[portlet]
            out.append('Removed %s portlet from right column.' % portlet) 
        if portlet in left:
            del left[portlet]
            out.append('Removed %s portlet from left column.' % portlet)
            
    out.append('Ran all uninstall steps.')
    
    return "\n".join(out)
