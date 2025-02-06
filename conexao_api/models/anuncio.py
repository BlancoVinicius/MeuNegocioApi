from typing import List
from  django.db import models

class SaleTerm(models.Model):
    id = "WARRANTY_TYPE",
    name = "Tipo de garantia"
    value_id = models.IntegerField(null=True)
    value_name = models.CharField(max_length=50)
    values = models.JSONField(null=True)

class Atributos(models.Model):
    terms_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    value_id = models.CharField(max_length=20, blank=True, null=True)
    value_name = models.CharField(max_length=255)
    values = models.JSONField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    category_id = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField(blank=False,null=False)
    condition = models.CharField(max_length=20)
    pictures = models.ImageField(upload_to='media/product_pictures/')
    description = models.TextField()
    attributes = models.ManyToManyField('Atributos')
    # atributos_lista: List[Atributos] = []


    def __str__(self):
        return self.title
    
class Anuncio(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    currency_id = "BRL"
    buying_mode = "buy_it_now"
    listing_type_id = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    description = models.TextField()
    shipping = models.JSONField()
    sale_term = models.CharField(max_length=20)
    warranty = models.CharField(max_length=255)
    sale_terms = models.ManyToManyField('SaleTerm')