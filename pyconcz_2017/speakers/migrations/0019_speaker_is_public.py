# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0018_auto_20170503_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]