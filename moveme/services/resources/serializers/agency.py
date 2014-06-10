from rest_framework import serializers

from .nextbus import NextBusTagSerializer


class AgencySerializer(NextBusTagSerializer):
    title = serializers.SerializerMethodField('get_title')
    region_title = serializers.SerializerMethodField('get_region_title')

    def get_title(self, obj):
        return obj.attrs.get('title')

    def get_region_title(self, obj):
        return obj.attrs.get('regionTitle')

