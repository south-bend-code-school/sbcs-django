# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20160906_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
