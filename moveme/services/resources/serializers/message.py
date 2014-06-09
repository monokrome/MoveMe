from rest_framework import serializers

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
    id = serializers.SerializerMethodField('get_id')
    creator = serializers.SerializerMethodField('get_creator')
    priority = serializers.SerializerMethodField('get_priority')

    send_to_buses = serializers.SerializerMethodField('get_send_to_buses')

    start_boundary = serializers.SerializerMethodField('get_start_boundary')
    end_boundary = serializers.SerializerMethodField('get_end_boundary')

    text = serializers.SerializerMethodField('get_text')

    def get_id(self, obj):
        return obj.attrs['id']

    def get_creator(self, obj):
        return obj.attrs.get('creator')

    def get_priority(self, obj):
        return obj.attrs['priority']

    def get_send_to_buses(self, obj):
        return obj.attrs['sendToBuses']

    def get_start_boundary(self, obj):
        return obj.attrs.get('startBoundary')

    def get_end_boundary(self, obj):
        return obj.attrs.get('endBoundary')

    def get_text(self, obj):
        return TextSerializer(obj, many=False).data


class RouteMessageSerializer(NextBusTagSerializer):
    message = serializers.SerializerMethodField('get_message')

    def get_message(self, obj):
        return MessageSerializer(
            obj.message,
            many=False
        ).data

