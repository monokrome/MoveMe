from . import nextbus
from .serializers.schedule import ScheduleSerializer


class ScheduleViewSet(nextbus.NextBusViewSet,
        nextbus.NextBusDetailMixin,
        nextbus.NextBusListMixin):

    root_tag_name = 'route'
    retrieve_command = 'schedule'
    retrieve_as_list = True

    serializer_class = ScheduleSerializer

