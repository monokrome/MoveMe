from rest_framework.exceptions import ParseError

from . import nextbus
from .serializers.vehicle import VehicleSerializer


class VehicleViewSet(nextbus.NextBusViewSet,
        nextbus.NextBusDetailMixin):

    root_tag_name = 'vehicle'
    retrieve_as_list = True
    retrieve_command = 'vehicleLocations'

    serializer_class = VehicleSerializer

    def get_url(self, request, pk=None):
        if 'time' not in request.GET:
            raise ParseError('The `time` field is required.')

        base_url = super(VehicleViewSet, self).get_url(request, pk)
        return base_url + '&t=' + request.GET['time']
