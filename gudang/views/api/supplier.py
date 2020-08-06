"""Area API view."""
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import is_expanded, FlexFieldsModelViewSet

from rest_framework import filters, viewsets, decorators, status
from rest_framework.settings import api_settings
from rest_framework.response import Response

from gudang.models import Supplier, DetailSupplier
from gudang.services import barang_service

from gudang.serializers.supplier import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    """Barang API."""
    queryset = Supplier.objects.order_by('nama')
    serializer_class = SupplierSerializer
    search_fields = ['nama']
    filter_backends = (filters.SearchFilter,)

    @decorators.action(detail=False, methods=['post'])
    def detail_supplier(self, request):
        """Get store by logged in member."""
        # try:
        data = request.data
        supplier = data['supplier']
        barang = data['barang']
        total = data['total']
        barang_service.supplier_barang(barang, total)
        barang_service.supplier(supplier,barang,total)
        serializer = MyStoreSerializer(store)
        return Response({"status": "Success"})
        # except:
        #     return Response({"status": "Error"})
        
