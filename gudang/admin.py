from django.contrib import admin

# Register your models here.
from gudang.models import Barang,DetailDistributor,DetailSupplier,Distributor,Supplier

class BarangAdmin(admin.ModelAdmin):
    """Barang admin."""
    list_display = ('nama', 'harga', 'stok')
    readonly_fields = ('stok',)
    search_fields = ('nama',)

class SupplierAdmin(admin.ModelAdmin):
    """Supplier admin."""
    pass

class DistributorAdmin(admin.ModelAdmin):
    """Distributor admin."""
    pass

class DetailDistributorAdmin(admin.ModelAdmin):
    """Detail distributor admin."""

class DetailSupplierAdmin(admin.ModelAdmin):
    """Detail Supplier admin."""

admin.site.register(Barang, BarangAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(DetailDistributor, DetailDistributorAdmin)
admin.site.register(DetailSupplier, DetailSupplierAdmin)


admin.site.site_title = "Gudang"
admin.site.site_header = "Gudang"
