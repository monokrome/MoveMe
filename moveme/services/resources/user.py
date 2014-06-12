from django.contrib.gis.geoip import GeoIP
from django.http import Http404

from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from django.conf import settings

from .serializers.user import UserSerializer


LOCALHOST_LOCATION_ALIAS = getattr(
    settings,
    'LOCALHOST_LOCATION_ALIAS',
    'google.com'
)


class UserViewSet(viewsets.ViewSet):
    """ Information about users. """

    serializer_class = UserSerializer

    def get_user_ip(self, request):
        forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR')

        if forwarded_ip:
            try:
                last_index = forwarded_ip.index(',')
            except ValueError:
                last_index = len(forwarded_ip) - 1

            ip_address = forwarded_ip[0:last_index]

        else:
            ip_address = request.META.get('REMOTE_ADDR')

        return ip_address

    def get_current_user(self, request):
        ip_address = self.get_user_ip(request)

        # Can not geolocate 'localhost', so use this for development instead.
        if ip_address[0:8] == '127.0.0.':
            ip_address = LOCALHOST_LOCATION_ALIAS

        location = GeoIP().lat_lon(ip_address)

        if location:
            (latitude, longitude) = location

            location = {
                'latitude': latitude,
                'longitude': longitude,
            }

        return {
            'ip_address': ip_address,
            'location': location
        }

    def list(self, request):
        users = [
            self.get_current_user(request),
        ]

        serializer = self.serializer_class(
            users,
            many=True
        ) 

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if pk != 'current':
            raise Http404('The specified user does not exist.')

        user = self.get_current_user(request)

        serializer = self.serializer_class(
            user,
            many=False
        ) 

        return Response(serializer.data)
