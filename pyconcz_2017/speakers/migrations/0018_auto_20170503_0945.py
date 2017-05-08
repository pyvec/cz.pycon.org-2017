# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0017_auto_20170206_1928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'ordering': ('display_position', 'full_name')},
        ),
        migrations.AddField(
            model_name='speaker',
            name='display_position',
            field=models.PositiveSmallIntegerField(default=0, help_text='sort order on frontend displays'),
        ),
    ]
