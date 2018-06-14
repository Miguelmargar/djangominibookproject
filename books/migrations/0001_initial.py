# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('author', models.CharField(max_length=254)),
                ('isbn', models.CharField(max_length=254)),
                ('notes', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
