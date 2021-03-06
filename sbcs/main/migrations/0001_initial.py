# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BioPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipFile', models.FileField(upload_to='/biopages')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('birthday', models.DateTimeField()),
                ('quote', models.CharField(blank=True, max_length=1000, null=True)),
                ('bioPage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.BioPage')),
            ],
        ),
    ]
