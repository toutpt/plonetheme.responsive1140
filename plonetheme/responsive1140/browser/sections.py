from plone.app.layout.viewlets import common
from plone.memoize import view
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class GlobalSectionsViewlet(common.GlobalSectionsViewlet):
    """Override to make it responsive"""
    index = ViewPageTemplateFile('sections.pt')

    def addClass(self, tab):
        """add css class to the tab element"""
        selected_tab=self.selected_portal_tab
        tid = tab[u'id']
        nbTabs = self.how_many_tabs()
        cssc = ''
        div = 12/nbTabs
        if nbTabs>12 or div == 1:
            cssc = 'onecol'
        elif div == 2:
            cssc = 'twocol'
        elif div == 3:
            cssc = 'threecol'
        elif div == 4:
            cssc = 'fourcol'
        elif div == 6:
            cssc = 'sixcol'
        elif div == 12:
            cssc = 'twelvecol'

        if selected_tab == tid:
            cssc += ' selected'
        else:
            cssc += ' plain'

        if self.islast(tab):
            cssc += ' last'

        return cssc

    @view.memoize
    def how_many_tabs(self):
        return len(self.portal_tabs)
    
    def islast(self, tab):
        return tab == self.portal_tabs[-1]
