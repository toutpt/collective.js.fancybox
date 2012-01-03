import os
from Globals import DTMLFile

from Products.Five.browser import BrowserView
this_dir = os.path.dirname(os.path.abspath(__file__))

fancybox_dir =  os.path.join(this_dir, 'fancybox')

# Don't add ".dtml" to the file name
# File on filesystem is "mystyles.css.dtml", enter "mystyles.css" here
fancybox_css_dtml = DTMLFile('jquery.fancybox.css', fancybox_dir)

class DTMLResource(BrowserView):     

    def fancybox_css(self, *args, **kw):
        template = fancybox_css_dtml.__of__(self.context)
        return template(context=self.context)        
