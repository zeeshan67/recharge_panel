# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recharge_panel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=500, null=True, blank=True)),
                ('lastname', models.CharField(max_length=500, null=True, blank=True)),
                ('company', models.CharField(max_length=500, null=True, blank=True)),
                ('username', models.CharField(max_length=500, null=True, blank=True)),
                ('email_id', models.CharField(max_length=500, null=True, blank=True)),
                ('phonenumber', models.CharField(max_length=12, null=True, blank=True)),
                ('address', models.CharField(max_length=1000, null=True, blank=True)),
                ('pin_code', models.CharField(max_length=500, null=True, blank=True)),
                ('city', models.CharField(max_length=500, null=True, blank=True)),
                ('state', models.CharField(max_length=500, null=True, blank=True)),
                ('country', models.CharField(max_length=500, null=True, blank=True)),
                ('passkey', models.CharField(max_length=256, null=True, blank=True)),
                ('cpasskey', models.CharField(max_length=256, null=True, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MyOrder',
        ),
    ]
