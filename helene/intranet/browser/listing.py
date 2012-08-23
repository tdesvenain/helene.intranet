from collective.edm.listing.listingoptions import DefaultListingOptions

class HeleneListingRights(DefaultListingRights):

    def globally_show_author(self):
        """View cut column
        """
        return False


class HeleneListingOptions(DefaultListingOptions):

    sort_mode = 'auto'
    default_sort_on = 'sortable_title'
    default_sort_order = 'asc'
    allow_edit_popup = True

