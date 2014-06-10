from rest_framework.exceptions import ParseError

from . import nextbus
from .serializers.vehicle import VehicleSerializer


class VehicleViewSet(nextbus.NextBusViewSet,
        nextbus.NextBusListMixin):

    root_tag_name = 'vehicle'
    list_command = 'vehicleLocations'

    serializer_class = VehicleSerializer

    def get_time(self, request):
        if 'time' in request.GET:
            try:
                time = int(request.GET['time'])
            except ValueError:
                raise ParseError('The `time` filter must be an integer.')
        else:
            time = 0

        return time

    def get_route(self, request):
        if not 'route' in request.GET:
            raise ParseError('A `route` filter must be provided.')

        return request.GET['route']

    def get_url(self, request, pk=None):
        """ Allow a 'time' filter for providing seconds since last checked. """

        time = self.get_time(request)
        route = self.get_route(request)

        base_url = super(VehicleViewSet, self).get_url(request, pk)
        return base_url + '&t={0}&r={1}'.format(time, route)

