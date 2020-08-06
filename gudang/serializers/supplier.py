"""Area serializer module."""
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from gudang.models import Supplier


class SupplierSerializer(FlexFieldsModelSerializer):
    class Meta:  # noqa D106
        model = Supplier
        fields = '__all__'
