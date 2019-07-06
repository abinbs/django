from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=100,decimal_places=2)
    summary=models.TextField(blank=False,null=True)
    featured=models.BooleanField()
    img=models.ImageField(upload_to='images/')
