"""Bolu Urls."""
from django.conf import settings
from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from gudang.views.api import barang as api_barang
from gudang.views.api import supplier as api_supplier
from gudang.views.api import distributor as api_distributor

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'barang', api_barang.BarangViewSet)
router.register(r'supplier', api_supplier.SupplierViewSet)
router.register(r'distributor', api_distributor.DistributorViewSet)


urlpatterns = [
    path('v1/', include((router.urls, 'api_views'), )),
]