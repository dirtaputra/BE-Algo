from django.db import models

# Create your models here.


class Supplier(models.Model):
    
    nama = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Distributor(models.Model):

    nama = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

class Barang(models.Model):
    
    nama = models.CharField(max_length=50)
    harga = models.FloatField(default=0)
    stok = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nama

class DetailSupplier(models.Model):

    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    barang = models.ForeignKey('Barang', on_delete=models.CASCADE)
    total = models.PositiveSmallIntegerField(default=0)



class DetailDistributor(models.Model):

    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    barang = models.ForeignKey('Barang', on_delete=models.CASCADE)
    total =  models.PositiveSmallIntegerField(default=0)
    


