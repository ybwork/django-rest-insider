from rest_framework import serializers

from buildings.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = (
            'name',
            'region',
            'district',
            'city',
            'country',
            'video',
            'coordinates',
            'currency',
            'company_id'
        )
