from rest_framework import serializers

from ...fields import TreeAttrField
from .nextbus import NextBusTagSerializer


class VehicleSerializer(serializers.Serializer):
    route = TreeAttrField('routeTag')
    direction = TreeAttrField('dirTag')

    latitude = TreeAttrField('lat')
    longitude = TreeAttrField('lon')

    speed = TreeAttrField('speedKmHr')
    speed_units = serializers.SerializerMethodField('get_speed_units')

    heading = TreeAttrField('heading')

    seconds_since_reported = TreeAttrField('secsSinceReport')
    is_predictable = TreeAttrField('predictable')

    def get_speed_units(self, obj):
        return 'KmPh'

