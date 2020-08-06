"""Area API view."""
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import is_expanded, FlexFieldsModelViewSet

from rest_framework import filters, viewsets, decorators, status
from rest_framework.settings import api_settings
from rest_framework.response import Response

from gudang.models import Supplier

from gudang.serializers.supplier import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    """Barang API."""
    queryset = Supplier.objects.order_by('nama')
    serializer_class = SupplierSerializer
    search_fields = ['nama']
    filter_backends = (filters.SearchFilter,)
    

