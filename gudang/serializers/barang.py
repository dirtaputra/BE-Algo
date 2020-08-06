"""Area serializer module."""
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from gudang.models import Barang


class BarangSerializer(FlexFieldsModelSerializer):
    class Meta:  # noqa D106
        model = Barang
        fields = '__all__'
