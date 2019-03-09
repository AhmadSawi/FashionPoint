# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-08 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionpointapp', '0003_auto_20190308_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('rating', models.FloatField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('picture1', models.ImageField(blank=True, null=True, upload_to='projectimg/')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='projectimg/')),
                ('picture1Clicks', models.IntegerField(default=0)),
                ('picture2Clicks', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Polls',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='projectimg/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='poll',
            name='category',
            field=models.ManyToManyField(to='fashionpointapp.Category'),
        ),
    ]