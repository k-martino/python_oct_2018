# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-15 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user_login', '0004_auto_20181015_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email_address',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
