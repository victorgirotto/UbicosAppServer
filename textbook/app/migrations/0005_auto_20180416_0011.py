# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-16 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180416_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]