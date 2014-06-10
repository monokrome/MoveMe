from rest_framework import serializers
from ...fields import TreeAttrField


class NextBusTagSerializer(serializers.Serializer):
    tag = TreeAttrField('tag')

