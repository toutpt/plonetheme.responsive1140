from Products.CMFCore.utils import getToolByName

def upgrade(context):
    cssregistry = getToolByName(context, 'portal_css')
    removeid = '++theme++plonetheme.responsive1140/css/theme.css'
    cssregistry.unregisterResource(removeid)
    for stylesheet in ('++theme++plonetheme.responsive1140/css/1140.css',
                       '++theme++plonetheme.responsive1140/css/ie.css',
                       'public.css'):
        cssregistry.getResource(stylesheet).setMedia('')
    
    cssregistry.cookResources()
