# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2023-02-07 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
    ]