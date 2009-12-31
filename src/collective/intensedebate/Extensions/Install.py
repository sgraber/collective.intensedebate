from Products.CMFCore.utils import getToolByName

def uninstall(portal):
    'Uninstall portal_controlpanel configlet'
    
    out = []
    cp = getToolByName(portal, 'portal_controlpanel', None)

    # Remove the configlet from the portal control panel:
    if cp:
        if "IntenseDebateConfig" in [ c.id for c in cp._actions ]:
            cp.unregisterConfiglet("IntenseDebateConfig")
            out.append('Removed configlet for IntenseDebateConfig')
    
    out.append('Ran all uninstall steps.')
    
    return "\n".join(out)
