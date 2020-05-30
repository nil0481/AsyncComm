from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    zip_code = models.CharField(max_length=10, default="")


    def __str__(self):
        return self.name