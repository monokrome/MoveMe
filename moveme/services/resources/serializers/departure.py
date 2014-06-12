from rest_framework import serializers

from ...fields import TreeAttrField
from .nextbus import NextBusTagSerializer


class PredictionSerializer(serializers.Serializer):
    time = TreeAttrField('epochTime')

    seconds = TreeAttrField('seconds')
    minutes = TreeAttrField('minutes')

    direction = TreeAttrField('dirTag')

    is_departure = TreeAttrField('isDeparture')
    has_layover = TreeAttrField('affectedByLayover')

    vehicle = TreeAttrField('vehicle')
    block = TreeAttrField('block')
    trip = TreeAttrField('tripTag')


class DirectionSerializer(serializers.Serializer):
    title = TreeAttrField()
    predictions = serializers.SerializerMethodField('get_predictions')

    def get_predictions(self, obj):
        return PredictionSerializer(
            obj.find_all('prediction'),
            many=True
        ).data


class MessageSerializer(serializers.Serializer):
    text = TreeAttrField()
    priority = TreeAttrField()


class DepartureSerializer(serializers.Serializer):
    agency = TreeAttrField('agencyTitle')

    route = TreeAttrField('routeTitle')
    route_tag = TreeAttrField('routeTag')

    stop = TreeAttrField('stopTitle')
    stop_tag = TreeAttrField('stopTag')

    directions = serializers.SerializerMethodField('get_directions')
    messages = serializers.SerializerMethodField('get_messages')

    def get_directions(self, obj):
        return DirectionSerializer(
            obj.find_all('direction'),
            many=True
        ).data

    def get_messages(self, obj):
        return MessageSerializer(
            obj.find_all('message'),
            many=True
        ).data

