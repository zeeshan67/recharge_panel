
# Create your models here.
from django.db import models
from uuid import uuid4

from uuid import UUID
import uuid
from django_extensions.db.fields import UUIDField
from django.contrib.auth.models import User
from django.db import models
from oauth2client import client


class MyOrder(models.Model):
    # items = models.ManyToManyField(OrderItem, null=True, blank=True)
    # order_date = models.DateField(auto_now=True)
    # buyer = models.ForeignKey(Buyer)

    txnid = models.CharField(max_length=36, primary_key=True)
    amount = models.FloatField(null=True, blank=True,default=0.0)
    hash = models.CharField(max_length=500, null=True, blank=True)
    billing_name = models.CharField(max_length=500, null=True, blank=True)
    billing_street_address = models.CharField(max_length=500, null=True, blank=True)
    billing_country = models.CharField(max_length=500, null=True, blank=True)
    billing_state = models.CharField(max_length=500, null=True, blank=True)
    billing_city = models.CharField(max_length=500, null=True, blank=True)
    billing_pincode = models.CharField(max_length=500, null=True, blank=True)
    billing_mobile = models.CharField(max_length=500, null=True, blank=True)
    billing_email = models.CharField(max_length=500, null=True, blank=True)

    shipping_name = models.CharField(max_length=500, null=True, blank=True)
    shipping_street_address = models.CharField(max_length=500, null=True, blank=True)
    shipping_country = models.CharField(max_length=500, null=True, blank=True)
    shipping_state = models.CharField(max_length=500, null=True, blank=True)
    shipping_city = models.CharField(max_length=500, null=True, blank=True)
    shipping_pincode = models.CharField(max_length=500, null=True, blank=True)
    shipping_mobile = models.CharField(max_length=500, null=True, blank=True)
    shipping_rate = models.FloatField(null=False, blank=False, default=0.0)
    status = models.CharField(max_length=500, null=True, blank=True)
    shipping_email = models.CharField(max_length=500, null=True, blank=True)

    payment_method = models.CharField(max_length=1000,verbose_name='Payment-method')
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)


class UserMaster(models.Model):
    user_name = models.CharField(max_length=500, null=False, blank=False)
    gender = models.CharField(max_length=6, null=False, blank=False)
    mobile_number = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    def get_user(self):
        return self.user_name