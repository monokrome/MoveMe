from rest_framework import serializers

from ...fields import TreeAttrField
from .nextbus import NextBusTagSerializer


class AgencySerializer(NextBusTagSerializer):
    title = TreeAttrField()
    region_title = TreeAttrField('regionTitle')
