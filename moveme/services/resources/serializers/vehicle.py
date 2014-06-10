from rest_framework import serializers
from .nextbus import NextBusTagSerializer


class VehicleSerializer(serializers.Serializer):
    route = serializers.SerializerMethodField('get_route')
    direction = serializers.SerializerMethodField('get_direction')

    latitude = serializers.SerializerMethodField('get_latitude')
    longitude = serializers.SerializerMethodField('get_longitude')

    speed = serializers.SerializerMethodField('get_speed')
    speed_units = serializers.SerializerMethodField('get_speed_units')

    seconds_delayed = serializers.SerializerMethodField('get_seconds_delayed')
    is_predictable = serializers.SerializerMethodField('get_is_predictable')

    def get_route(self, obj):
        # TODO: Convert this into a hyperlink
        return obj.attrs.get('routeTag')

    def get_direction(self, obj):
        return obj.attrs.get('dirTag')

    def get_latitude(self, obj):
        return obj.attrs.get('lat')

    def get_longitude(self, obj):
        return obj.attrs.get('lon')

    def get_seconds_delayed(self, obj):
        return obj.attrs.get('secsSinceReport')

    def get_is_predictable(self, obj):
        return obj.attrs.get('predictable')

    def get_heading(self, obj):
        return obj.attrs.get('heading')

    def get_speed(self, obj):
        return obj.attrs.get('speedKmHr')

    def get_speed_units(self, obj):
        return 'KmPh'
