from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Vendor_Model(models.Model):
    name = models.CharField(max_length=20)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=150,unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()


    def __str__(self):
        return self.name
    

class Purchase_Order_Model(models.Model):
    po_number = models.CharField(max_length=150,unique=True)
    vendor = models.ForeignKey(Vendor_Model,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=150)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()


    def __str__(self):
        return self.po_number
    

class Historical_Performance_Model(models.Model):
    vendor = models.ForeignKey(Vendor_Model,on_delete=models.CASCADE)
    date = models.DateField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.vendor.name