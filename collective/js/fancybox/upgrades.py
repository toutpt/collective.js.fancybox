from Products.CMFCore.utils import getToolByName

def upgrade_to_1000(context):
    cssregistry = getToolByName(context, 'portal_css')
    jsregistry = getToolByName(context, 'portal_javascripts')
    setup = getToolByName(context, 'portal_setup')
    
    cssregistry.unregisterResource('jquery.fancybox.css')
    cssregistry.unregisterResource('++resource++collective.fancybox/jquery.fancybox.css')
    jsregistry.unregisterResource('++resource++collective.fancybox/jquery.fancybox.pack.js')
    
    setup.runImportStepFromProfile('profile-collective.js.fancybox:default',
                                   'cssregistry',
                                   run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile('profile-collective.js.fancybox:default',
                                   'jsregistry',
                                   run_dependencies=False,
                                   purge_old=False)
