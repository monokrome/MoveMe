from rest_framework import serializers


class NextBusTagSerializer(serializers.Serializer):
    tag = serializers.SerializerMethodField('get_tag')

    def get_tag(self, obj):
        return obj.attrs['tag']

