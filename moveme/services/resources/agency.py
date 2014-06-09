from . import nextbus
from .serializers.agency import AgencySerializer


class AgencyViewSet(nextbus.NextBusViewSet,
        nextbus.NextBusListMixin):

    tag_name = 'agency'
    require_agency = False

    serializer_class = AgencySerializer

