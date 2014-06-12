from rest_framework.exceptions import ParseError

from . import nextbus
from .serializers.prediction import PredictionSerializer


class PredictionViewSet(nextbus.NextBusViewSet,
        nextbus.NextBusListMixin):

    root_tag_name = 'prediction'
    list_command = 'predictions'

    serializer_class = PredictionSerializer

    def get_url(self, request, pk=None):
        """ Allow a 'time' filter for providing seconds since last checked. """

        if 'time' in request.GET:
            time = request.GET['time']
        else:
            time = 0

        base_url = super(PredictionViewSet, self).get_url(request, pk)
        return base_url + '&t=' + time

