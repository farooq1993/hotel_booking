from django.db import models
import random
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from location_field.models.plain import PlainLocationField

# Create your models here.

class creatuser(models.Model):
    username=models.CharField(max_length=100, null=True, blank=True)
    password=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username


        
class cityies(models.Model):
    city=models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.city

class Tours(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    city=models.ForeignKey(cityies, on_delete=models.CASCADE, null=True, blank=True)
    address=models.CharField(max_length=500, null=True, blank=False)
    Place_descriptions=models.CharField(max_length=1000, null=True, blank=False)
    place_img=models.ImageField()
    Event_img=models.ImageField()
    hotel_name=models.CharField(max_length=100, null=True, blank=True)
    amount=models.IntegerField()
    availble_date=models.DateTimeField(auto_now=False)
    hotel_star=models.IntegerField()
    hotel_rating=models.FloatField()
    discount_percent=models.IntegerField()
    offerlimited=models.IntegerField()

    def save(self, *args, **kwargs):
        super(Tours, self).save(*args, **kwargs)
        print(super)

    # class Meta:
    #     models='tours'
    def __str__(self):
        return str(self.amount) + self.address
    


#for room availble
class rooms(models.Model):
    room=models.IntegerField()

    def __str__(self):
        return str(self.room)







Adult_members = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    
)
class tourbooking(models.Model):
    hote_add=models.ForeignKey(Tours, on_delete=models.CASCADE, null=True, blank=True)
    booked_date=models.DateTimeField(auto_now=True)
    user_name=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=100, null=True, blank=True)
    phone=models.BigIntegerField(null=True, blank=True)
    email=models.EmailField()
    checkindate=models.DateTimeField(default=timezone.now)
    checkoutdate=models.DateTimeField(default=timezone.now)
    numberofadult=models.CharField(max_length=100,choices=Adult_members, null=True, blank=True)
    #amount=models.ForeignKey(Tours, on_delete=models.CASCADE, null=True, blank=True)
    amount=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    numberofrooms=models.IntegerField(null=True, blank=True)
    #total_amount=models.BigIntegerField()
    is_pay=models.BooleanField(default=False)
    #total=models.BigIntegerField()
    

    def __str__(self):
       return self.name

    
    
class payment(models.Model):
    
    name=models.CharField(max_length=100, null=True, blank=True)
    amount=models.ForeignKey(tourbooking, on_delete=models.CASCADE, null=True, blank=True)
    razorpay_id=models.CharField(max_length=100, null=True, blank=True)
    order_id=models.CharField(max_length=100, null=True, blank=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class weekenddeals(models.Model):
    hotel_name=models.ForeignKey(Tours, on_delete=models.CASCADE, null=True, blank=True)
    amount=models.BigIntegerField()

    def __str__(self):
        return self.hotel_name

class favoritedestination(models.Model):
    city=models.ForeignKey(cityies, on_delete=models.CASCADE, null=True, blank=True)
    destinations_name=models.CharField(max_length=200, blank=True, null=True)
    destination_img=models.ImageField(upload_to='images')
    description=models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.destinations_name