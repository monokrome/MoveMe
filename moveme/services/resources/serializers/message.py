from rest_framework import serializers

from ...fields import TreeAttrField
from .nextbus import NextBusTagSerializer


class TextSerializer(serializers.Serializer):
    standard = serializers.SerializerMethodField('get_standard')
    alternate = serializers.SerializerMethodField('get_alternate')
    phoneme = serializers.SerializerMethodField('get_phoneme')

    def get_standard(self, obj):
        text = obj.find('text')

        if text and text is not -1:
            return text.text

    def get_alternate(self, obj):
        text = obj.find('alternateText')

        if text and text is not -1:
            return text.text

    def get_phoneme(self, obj):
        text = obj.find('phonemeText')

        if text and text is not -1:
            return text.text


class MessageSerializer(serializers.Serializer):
    id = TreeAttrField()
    creator = TreeAttrField()
    priority = TreeAttrField()

    send_to_buses = TreeAttrField('sendToBuses')

    start_boundary = TreeAttrField('startBoundary')
    end_boundary = TreeAttrField('endBoundary')

    text = serializers.SerializerMethodField('get_text')

    def get_text(self, obj):
        return TextSerializer(obj, many=False).data


class RouteMessageSerializer(NextBusTagSerializer):
    message = serializers.SerializerMethodField('get_message')

    def get_message(self, obj):
        return MessageSerializer(
            obj.message,
            many=False
        ).data

