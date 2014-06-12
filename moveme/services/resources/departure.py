from rest_framework.exceptions import ParseError

from . import nextbus
from .serializers.departure import DepartureSerializer


class DepartureViewSet(nextbus.NextBusViewSet,
        nextbus.NextBusListMixin):

    root_tag_name = 'predictions'
    list_command = 'predictions'

    serializer_class = DepartureSerializer

    def get_url(self, request, pk=None):
        """ Provide a NextBus URL for prediction data. """

        if 'route' in request.GET:
            route = request.GET['route']
        else:
            raise ParseError('The `route` field is required.')

        if 'stop' in request.GET:
            stop = request.GET['stop']
        else:
            raise ParseError('The `stop` filter must be a valid stop id.')

        base_url = super(DepartureViewSet, self).get_url(request, pk)
        url = base_url + '&r=' + route + '&s=' + stop

        return url

