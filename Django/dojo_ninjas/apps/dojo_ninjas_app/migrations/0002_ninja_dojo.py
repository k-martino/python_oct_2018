# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-15 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas_app.Dojo'),
            preserve_default=False,
        ),
    ]
