# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-08 16:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fashionpointapp', '0007_auto_20190308_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('dateOfBirth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.AlterModelOptions(
            name='pollcomment',
            options={'verbose_name_plural': 'Poll Comments'},
        ),
        migrations.AlterModelOptions(
            name='postcomment',
            options={'verbose_name_plural': 'Post Comments'},
        ),
        migrations.AddField(
            model_name='poll',
            name='userPofile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fashionpointapp.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pollcomment',
            name='userPofile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fashionpointapp.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='userPofile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fashionpointapp.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postcomment',
            name='userPofile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fashionpointapp.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='userPofile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fashionpointapp.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='userPofile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fashionpointapp.UserProfile'),
            preserve_default=False,
        ),
    ]
