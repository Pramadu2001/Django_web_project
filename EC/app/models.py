from django.db import models

class products(models.Model):

    CATEGORY_CHOICES ={
          ('Mw','MensWear'),
          ('CW','CasualWear'),
          ('WW','WomensWear'),
          ('KW','KidsWear'),
          ('FW','FormalWear'),
          ('AC','Accessories'),
    }

    title =models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    material = models.TextField(default='')
    category =models.CharField(choices= CATEGORY_CHOICES,max_length=2)
    product_image =models.ImageField(upload_to= 'product')
    def __str__(self):
        return self.title
        
