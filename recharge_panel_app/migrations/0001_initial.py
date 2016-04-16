# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('order_date', models.DateField(auto_now=True)),
                ('txnid', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('amount', models.FloatField(default=0.0, null=True, blank=True)),
                ('hash', models.CharField(max_length=500, null=True, blank=True)),
                ('billing_name', models.CharField(max_length=500, null=True, blank=True)),
                ('billing_street_address', models.CharField(max_length=500, null=True, blank=True)),
                ('billing_country', models.CharField(max_length=500, null=True, blank=True)),
                ('billing_state', models.CharField(max_length=500, null=True, blank=True)),
                ('billing_city', models.CharField(max_length=500, null=True, blank=True)),
                ('billing_pincode', models.CharField(max_length=500, null=True, blank=True)),
                ('billing_mobile', models.CharField(max_length=500, null=True, blank=True)),
                ('billing_email', models.CharField(max_length=500, null=True, blank=True)),
                ('shipping_name', models.CharField(max_length=500, null=True, blank=True)),
                ('shipping_street_address', models.CharField(max_length=500, null=True, blank=True)),
                ('shipping_country', models.CharField(max_length=500, null=True, blank=True)),
                ('shipping_state', models.CharField(max_length=500, null=True, blank=True)),
                ('shipping_city', models.CharField(max_length=500, null=True, blank=True)),
                ('shipping_pincode', models.CharField(max_length=500, null=True, blank=True)),
                ('shipping_mobile', models.CharField(max_length=500, null=True, blank=True)),
                ('shipping_rate', models.FloatField(default=0.0)),
                ('status', models.CharField(max_length=500, null=True, blank=True)),
                ('shipping_email', models.CharField(max_length=500, null=True, blank=True)),
                ('payment_method', models.CharField(max_length=1000, verbose_name=b'Payment-method')),
                ('is_paid', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('is_accepted', models.BooleanField(default=False)),
            ],
        ),
    ]
