import copy
import operator

from . import nextbus
from .serializers.message import RouteMessageSerializer


# NOTE: Points, directions, paths, etc are all their own resource type in an
# ideal world. However, the data source doesn't allow us to split them up
# reasonably without a lot of extra work here.
class MessageViewSet(nextbus.NextBusViewSet,
        nextbus.NextBusListMixin,
        nextbus.NextBusDetailMixin):

    root_tag_name = 'route'
    retrieve_command = 'messages'

    serializer_class = RouteMessageSerializer

