# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-16 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionpointapp', '0012_auto_20190309_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, upload_to='cats'),
        ),
    ]
