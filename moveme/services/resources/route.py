import copy
import operator

from . import nextbus
from .serializers.route import RouteSerializer


# NOTE: Points, directions, paths, etc are all their own resource type in an
# ideal world. However, the data source doesn't allow us to split them up
# reasonably without a lot of extra work here.
class RouteViewSet(nextbus.NextBusViewSet,
        nextbus.NextBusListMixin,
        nextbus.NextBusDetailMixin):

    tag_name = 'route'
    serializer_class = RouteSerializer

