from django.db.models import F, Q, Value
from django.db.models.functions import Concat

from gudang.models import Barang, DetailSupplier, DetailDistributor, Supplier

class BarangService:
    """Service."""

    def supplier(self, supplier, barang, total):
        data = Supplier.objects.filter(id=supplier).first()
        print(data.id)
        DetailSupplier.objects.create(
            supplier=data.id,
            barang=barang,
            total=total,
        )

    def distributor(self, distributor, barang, total):
        DetailDistributor.objects.create(
            distributor=distributor,
            barang=barang,
            total=total,
        )

    def supplier_barang(self, barang, stok):
        dataBarang = Barang.objects.filter(id=barang).first()
        totalStok = dataBarang.stok + stok
        dataBarang.stok = totalStok
        dataBarang.save()
        return dataBarang

    def distributor_barang(self, barang, stok):
        dataBarang = Barang.objects.filter(id=barang).first()
        totalStok = dataBarang.stok - stok
        dataBarang.stok = totalStok
        dataBarang.save()
        return dataBarang

barang_service = BarangService()
