from rest_framework import serializers

from .nextbus import NextBusTagSerializer
from ...fields import TreeAttrField, TreeTextField


class StopSerializer(NextBusTagSerializer):
    content = TreeTextField()


class OverviewSerializer(serializers.Serializer):
    stops = serializers.SerializerMethodField('get_stops')

    def get_stops(self, obj):
        return StopSerializer(
            obj.find_all('stop'),
            many=True
        ).data

class TimedStopSerializer(NextBusTagSerializer):
    time = TreeTextField()
    epoch_time = TreeAttrField('epochTime')


class BlockSerializer(serializers.Serializer):
    id = TreeAttrField('blockID')
    stops = serializers.SerializerMethodField('get_stops')

    def get_stops(self, obj):
        return TimedStopSerializer(
            obj.find_all('stop'),
            many=True
        ).data

class ScheduleSerializer(NextBusTagSerializer):
    overview = serializers.SerializerMethodField('get_overview')
    blocks = serializers.SerializerMethodField('get_blocks')

    title = TreeAttrField('title')
    schedule_class = TreeAttrField('scheduleClass')
    service_class = TreeAttrField('serviceClass')

    # TODO: direction?

    def get_overview(self, obj):
        return OverviewSerializer(
            obj.find('header'),
            many=False
        ).data

    def get_blocks(self, obj):
        return BlockSerializer(
            obj.find_all('tr'),
            many=True
        ).data

