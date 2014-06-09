from .nextbus import NextBusViewSet


class AgencyViewSet(NextBusViewSet):
    command = 'agencyList'

    def parse_agency(self, agency):
        """ Translate an item in the tree into an agency object. """

        return agency.attrs

    def parse_tree(self, tree):
        agencies = tree.find_all('agency')
        return map(self.parse_agency, agencies)

