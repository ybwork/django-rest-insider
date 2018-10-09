from rest_framework import serializers


class PricesSerializer(serializers.Serializer):
    prices = serializers.FileField()
