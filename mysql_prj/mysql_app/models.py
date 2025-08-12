from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class UserRegistration(models.Model):
    #user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=False)
    email = models.EmailField()
    password=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table = "userregistration"

class additem(models.Model):
    itemname = models.CharField(max_length=100, blank=False, unique=True)
    price = models.IntegerField(blank=False)
    category = (('Furniture', 'Furniture'), ('Electronics', 'Electronics'), ('Books', 'Books'))
    file_category = models.CharField(max_length=50, choices=category, blank=False)
    if(file_category=='Furniture'):
        sub_category = (('chairs', 'chairs'), ('sofa', 'sofa'), ('tables', 'tables'))
        file_subcategory = models.CharField(max_length=50, choices=sub_category, blank=False)
    if (file_category == 'Books'):
        sub_category = (('comics', 'comics'), ('studymaterials', 'studymaterials'), ('horror', 'horror'))
        file_subcategory = models.CharField(max_length=50, choices=sub_category, blank=False)
    if (file_category == 'Electronics'):
        sub_category = (('electricappliances', 'electricappliances'), ('gymappliances', 'gymappliances'))
        file_subcategory = models.CharField(max_length=50, choices=sub_category, blank=False)

    quantity = models.IntegerField(blank=False)
    attachment = models.ImageField(upload_to = "images/")
    description = models.TextField(max_length=255, blank=False)
    fileuploadtime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "additem"


class cartpage(models.Model):

    itemname = models.CharField(max_length=100, blank=False, unique=True)
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)
    attachment = models.ImageField(upload_to = "cartimages/")
    fileuploadtime = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
    class Meta:
        db_table = "cartpage"
class cartpage1(models.Model):
    itemname = models.CharField(max_length=100, blank=False, unique=True)
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)
    attachment = models.ImageField(upload_to = "cartimages/")
    fileuploadtime = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
    class Meta:
        db_table = "cartpage1"









class Order(models.Model):
    first_name = models.CharField(max_length=60,blank=False)
    last_name = models.CharField(max_length=60,blank=False)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=150,blank=False)
    postal_code = models.CharField(max_length=30,blank=False)
    city = models.CharField(max_length=100,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(additem, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    #quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

