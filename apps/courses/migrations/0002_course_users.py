# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(to='login_reg.User'),
        ),
    ]
