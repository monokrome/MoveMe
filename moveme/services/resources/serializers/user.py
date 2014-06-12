from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    ip_address = serializers.CharField()

    lat = serializers.DecimalField(source='location.latitude')
    lon = serializers.DecimalField(source='location.longitude')

