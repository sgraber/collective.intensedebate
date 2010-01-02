Introduction
============

This product integrates the 'IntenseDebate'_ commenting system into 'Plone'_.

Plone's default commenting system is basic and sometimes leaves people wanting
more features.  In Plone, it's hard to find new comments, administer comments,
and block unwanted text or users.  This package, collective.intensedebate, 
attempts to solve this problem along with bringing additional features to the
commenting system by replacing Plone's default commenting with the 
'IntenseDebate'_ commenting system.

IntenseDebate comes with the following 'features'_:

* 'Akismet'_ Spam Filtering
* Comment Threading
* Reply-by-Email
* Email Notifications
* Commenter Profiles
* Comment Moderation / Blacklisting
* Reputation Points & Comment Voting
* Plugins API
* Logins via OpenID, Facebook, Twitter
* Widgets
* Twitter
* RSS Reading & Tracking
* HTML Formatting
* 'Gravatar'_ support
* And Much More!

IntenseDebate also supports import/export of comments so you can take your
comments with you if you decide to move to a different commenting system.

Another popular commenting system used on many sites is 'DISQUS'_ and it 
allows importing of comments from other commenting systems such as 
IntenseDebate.  Plone also has a product called 'collective.disqus'_ for 
integrating this commenting system into Plone.  collective.intensedebate
borrows heavily from its codebase and thanks go out to 'Wojciech Lichota'_
for the initial collective.disqus product.


Installation
============

Installation on your Plone site is pretty straight forward:

1. Create account on `IntenseDebate`_
2. Add you website in IntenseDebate administration panel
3. Add `collective.intensedebate` to your buildout:
  
    eggs =
        collective.intensedebate
    
    zcml = 
        collective.intensedebate

4. Inside your Plone site, use *Add products* in *Site Setup* or 
*QuickInstaller* to activate it.

The installer will replace Plone's commenting viewlet with a viewlet of its
own.  The product also ships with three IntenseDebate portlets that you can
use to show commenting statistics:

* A list of your top commenters
* Your most popular / commented on content
* The latest comments for your site


Configuration
=============

Go to *Site Setup* -> *IntenseDebate commenting system* control panel form and 
configure *Website short name*.

Current version of collective.intensedebate doesn't migrate comments. This
is handled from the 'IntenseDebate'_ website and not from inside Plone.

IntenseDebate comments should be visible in all content that has commenting
enabled within Plone.  If you want to turn off commenting, adjust your portal
settings accordingly.

For portlets, simply install them like you would for a normal portlet.


Contributors
============

* Project initiated by Shane Graber
* Code heavily borrowed from 'Wojciech Lichota'_ and 'collective.disqus'_


To Do
=====

O  Add a view to Collections view for showing comment stats - something like "Comments: ##"
X  Hide Plone comments viewlet properly. 01/01/10
X  Uninstall the IntenseDebate viewlet and re-enable Plone comments viewlet. 01/01/10
X  Uninstall the IntenseDebate configlet properly. 01/01/10
X  Replace portlet code so that it's configurable from the control panel configlet. 12/31/09
X  Make each portlet configurable from @@manage-portlets. 01/01/10


Links
=====

.. _IntenseDebate: http://intensedebate.com/home
.. _Plone: http://plone.org
.. _features: http://intensedebate.com/features
.. _Akismet: http://akismet.com/
.. _Gravitar: http://www.gravatar.com
.. _DISQUS: http://disqus.com
.. _Wojciech Lichota: http://lichota.pl/blog
.. _collective.disqus: http://plone.org/products/collective.disqus