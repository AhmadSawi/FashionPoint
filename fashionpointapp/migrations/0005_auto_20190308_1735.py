# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-08 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionpointapp', '0004_auto_20190308_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='picture1',
            field=models.ImageField(blank=True, upload_to='projectimg/'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='picture2',
            field=models.ImageField(blank=True, upload_to='projectimg/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='projectimg/'),
        ),
    ]
