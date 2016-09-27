# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-09-26 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20160926_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='description',
        ),
        migrations.AddField(
            model_name='talk',
            name='abstract',
            field=models.TextField(default='', help_text='Full description of your talk. How would you describe yourtalk to the audience?'),
            preserve_default=False,
        ),
    ]
