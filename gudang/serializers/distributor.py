"""Area serializer module."""
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from gudang.models import Distributor


class DistributorSerializer(FlexFieldsModelSerializer):
    class Meta:  # noqa D106
        model = Distributor
        fields = '__all__'
