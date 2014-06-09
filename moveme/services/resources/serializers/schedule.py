from rest_framework import serializers

from .nextbus import NextBusTagSerializer


class StopSerializer(NextBusTagSerializer):
    content = serializers.SerializerMethodField('get_content')

    def get_content(self, obj):
        return obj.text


class OverviewSerializer(serializers.Serializer):
    stops = serializers.SerializerMethodField('get_stops')

    def get_stops(self, obj):
        # TODO: Not sure what this is all about.
        return StopSerializer(
            obj.find_all('stop'),
            many=True
        ).data


class TimedStopSerializer(NextBusTagSerializer):
    time = serializers.SerializerMethodField('get_time')
    epoch_time = serializers.SerializerMethodField('get_epoch_time')

    def get_time(self, obj):
        return obj.text

    def get_epoch_time(self, obj):
        return obj.attrs['epochTime']


class BlockSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField('get_id')
    stops = serializers.SerializerMethodField('get_stops')

    def get_id(self, obj):
        return obj.attrs['blockID']

    def get_stops(self, obj):
        # TODO: Not sure what this is all about.
        return TimedStopSerializer(
            obj.find_all('stop'),
            many=True
        ).data

class ScheduleSerializer(NextBusTagSerializer):
    overview = serializers.SerializerMethodField('get_overview')
    blocks = serializers.SerializerMethodField('get_blocks')

    title = serializers.SerializerMethodField('get_title')
    schedule_class = serializers.SerializerMethodField('get_schedule_class')
    service_class = serializers.SerializerMethodField('get_service_class')

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

    def get_title(self, obj):
        return obj.attrs['title']

    def get_schedule_class(self, obj):
        return obj.attrs['scheduleClass']

    def get_service_class(self, obj):
        return obj.attrs['serviceClass']

    def get_direction(self, obj):
        return obj.attrs['direction']

