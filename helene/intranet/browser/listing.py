from collective.edm.listing.listingoptions import DefaultListingOptions
from collective.edm.listing.listingrights import DefaultListingRights

class ListingRights(DefaultListingRights):
    """ """

    def globally_show_author(self):
        """View cut column
        """
        return False

    def globally_can_cut(self, brains):
        """View cut column
        """
        return self.candeletecontents

    def globally_can_delete(self, brains):
        if not self.context.isTrashcanOpened():
            return False

        return super(ListingRights, self).globally_can_cut(brains)

    def globally_show_state(self, brains):
        return False


class ListingOptions(DefaultListingOptions):

    sort_mode = 'manual'
    default_sort_on = 'sortable_title'
    default_sort_order = 'asc'
    allow_edit_popup = True
