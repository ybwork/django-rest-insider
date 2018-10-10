from rest_framework import serializers


class PricesSerializer(serializers.Serializer):
    schema = serializers.FileField()
