# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-17 04:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0005_auto_20181015_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email_address', models.EmailField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('age', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(125)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
