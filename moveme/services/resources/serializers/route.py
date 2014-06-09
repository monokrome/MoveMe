from rest_framework import serializers

from .nextbus import NextBusTagSerializer


class PointSerializer(serializers.Serializer):
    lat = serializers.SerializerMethodField('get_latitude')
    lon = serializers.SerializerMethodField('get_longitude')

    def get_latitude(self, obj):
        return float(obj.attrs['lat'])

    def get_longitude(self, obj):
        return float(obj.attrs['lon'])


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
    title = serializers.SerializerMethodField('get_title')
    lat = serializers.SerializerMethodField('get_latitude')
    lon = serializers.SerializerMethodField('get_longitude')
    id = serializers.SerializerMethodField('get_id')

    # FIXME: NextBus API won't split out titles for duplicate records.

    # Right now, we are simply using get() in order to return None for
    # non-existing keys, but we should temporarily cache these values
    # in order to preserve them in repeat objects.
    def get_title(self, obj):
        return obj.attrs.get('title')

    def get_latitude(self, obj):
        return obj.attrs.get('lat')

    def get_longitude(self, obj):
        return obj.attrs.get('lon')

    def get_id(self, obj):
        return obj.attrs.get('stopId')


class DirectionSerializer(NextBusTagSerializer):
    title = serializers.SerializerMethodField('get_title')
    # stops = serializers.SerializerMethodField('get_stops')
    name = serializers.SerializerMethodField('get_name')
    user_important = serializers.SerializerMethodField('get_user_important')

    def get_title(self, obj):
        return obj.attrs['title']

    def get_name(self, obj):
        return obj.attrs['name']

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

