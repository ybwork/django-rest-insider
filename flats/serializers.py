from rest_framework import serializers

from flats.models import Flat


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = (
            'house',
            'price',
            'number',
            'entrance',
            'floor',
            'status',
            'clone_for_flats',
            'type'
        )
        many = True