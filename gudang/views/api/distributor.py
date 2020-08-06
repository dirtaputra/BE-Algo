"""Area API view."""
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import is_expanded, FlexFieldsModelViewSet

from rest_framework import filters, viewsets, decorators, status
from rest_framework.settings import api_settings
from rest_framework.response import Response

from gudang.models import Distributor

from gudang.serializers.distributor import DistributorSerializer


class DistributorViewSet(viewsets.ModelViewSet):
    """Distributor API."""
    queryset = Distributor.objects.order_by('nama')
    serializer_class = DistributorSerializer
    search_fields = ['nama']
    filter_backends = (filters.SearchFilter,)
    

