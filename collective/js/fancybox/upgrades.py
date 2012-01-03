from Products.CMFCore.utils import getToolByName

def upgrade_to_1000(context):
    cssregistry = getToolByName(context, 'portal_css')
    setup = getToolByName(context, 'portal_setup')
    
    cssregistry.unregisterResource('jquery.fancybox.css')
    
    setup.runImportStepFromProfile('profile-collective.js.fancybox:default',
                                   'cssregistry',
                                   run_dependencies=False,
                                   purge_old=False)
