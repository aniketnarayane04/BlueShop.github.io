from django.db import models

# Create your models here.
class Carousel(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()

    def __str__(self):
        return self.name

class Mobiles(models.Model):
    mbl_name = models.CharField(max_length= 200)
    price = models.IntegerField()
    brand = models.CharField(max_length=50)
    desc = models.TextField()
    img1 = models.ImageField()
    color = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    rating = models.FloatField()
    order = models.BooleanField(null=True, default=False)
    cart = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.mbl_name 