# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-17 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionpointapp', '0015_auto_20190317_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='nod',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='nol',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
