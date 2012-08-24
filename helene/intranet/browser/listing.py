from collective.edm.listing.listingoptions import DefaultListingOptions
from collective.edm.listing.listingrights import DefaultListingRights

class ListingRights(DefaultListingRights):
    """ """

    def globally_show_author(self):
        """View cut column
        """
        return False

    def globally_can_delete(self, brains):
        if not self.context.isTrashcanOpened():
            return False

        return super(ListingOptions, self).globally_can_delete()


class ListingOptions(DefaultListingOptions):

    sort_mode = 'auto'
    default_sort_on = 'sortable_title'
    default_sort_order = 'asc'
    allow_edit_popup = True
