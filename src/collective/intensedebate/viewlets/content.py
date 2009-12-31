# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase
from plone.memoize.instance import memoize

from collective.intensedebate.browser.configlet import IIntenseDebateSettings

class IntenseDebateViewlet(ViewletBase):
    """
    Viewlet for IntenseDebate comment system.  
    """
    index = ViewPageTemplateFile("intensedebate_panel.pt")
    
    def update(self):
        """
        Update parameters used to render template.
        """
        super(IntenseDebateViewlet, self).update()
        portal_discussion = getToolByName(self.context, 'portal_discussion', None)
        
        self.is_discussion_allowed = False
        if portal_discussion is not None:
            self.is_discussion_allowed = portal_discussion.isDiscussionAllowedFor(aq_inner(self.context))
            
        portal_url = getToolByName(self.context, 'portal_url')
        portal = portal_url.getPortalObject()
        self.settings = IIntenseDebateSettings(portal)


    def render_js_settings(self):
        """
        Config for IntenseDebate embed.

        idcomments_post_id: This is the unique identifier of the post or page. 
        This is what keeps the comments set on this page different than comments
        set on another page. The default value is the url of the page.
        Manually set here to remove arbitrary views Plone places on content
        objects.
        
        idcomments_post_url: This is the url of the post or page. This is url 
        Intense Debate will link to in rss feeds and on IntenseDebate.com. The 
        default is the current page's url.
        
        idcomments_post_title: This is title of the post or page. This is the 
        title that will be displayed in rss feeds and on IntenseDebate.com. The 
        default value is the title of the current page.
        """
        obj_url = aq_inner(self.context).absolute_url()
        
        result =  'var idcomments_acct = "%s";\n' % self.settings.forum_id
        result += 'var idcomments_post_url = "%s";\n' % obj_url
        result += 'var idcomments_post_id;\n'        
        return result
