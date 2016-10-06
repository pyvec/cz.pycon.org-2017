# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-10-06 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0007_auto_20161005_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='talks',
            field=models.ManyToManyField(blank=True, to='speakers.Talk'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='workshops',
            field=models.ManyToManyField(blank=True, to='speakers.Workshop'),
        ),
    ]
