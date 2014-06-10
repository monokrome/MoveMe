from rest_framework import serializers

from ...fields import TreeAttrField
from .nextbus import NextBusTagSerializer


class PointSerializer(serializers.Serializer):
    lat = TreeAttrField()
    lon = TreeAttrField()


class PathSerializer(serializers.Serializer):
    points = serializers.SerializerMethodField('get_points')

    def get_points(self, obj):
        return PointSerializer(
            obj.find_all('point'),
            many=True
        ).data


class StopSerializer(NextBusTagSerializer):
    pass


class DetailedStopSerializer(StopSerializer):
    id = TreeAttrField('stopId')
    title = TreeAttrField()

    lat = TreeAttrField()
    lon = TreeAttrField()


class DirectionSerializer(NextBusTagSerializer):
    title = TreeAttrField()
    name = TreeAttrField()

    stops = serializers.SerializerMethodField('get_stops')
    user_important = serializers.SerializerMethodField('get_user_important')

    def get_user_important(self, obj):
        """ Returns whether or not this is an important step for a user. """
        return obj.attrs['useForUI'] == 'true'

    def get_stops(self, obj):
        return StopSerializer(
            obj.find_all('stop'),
            many=True
        ).data


class RouteSerializer(NextBusTagSerializer):
    stops = serializers.SerializerMethodField('get_stops')
    directions = serializers.SerializerMethodField('get_directions')
    paths = serializers.SerializerMethodField('get_paths')

    def get_stops(self, obj):
        return DetailedStopSerializer(
            obj.find_all('stop'),
            many=True
        ).data

    def get_directions(self, obj):
        return DirectionSerializer(
            obj.find_all('direction'),
            many=True
        ).data

    def get_paths(self, obj):
        return PathSerializer(
            obj.find_all('path'),
            many=True
        ).data

