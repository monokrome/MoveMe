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
        """ Allow a 'time' filter for providing seconds since last checked. """

        if 'time' in request.GET:
            time = request.GET['time']
        else:
            time = 0

        base_url = super(VehicleViewSet, self).get_url(request, pk)
        return base_url + '&t=' + time

