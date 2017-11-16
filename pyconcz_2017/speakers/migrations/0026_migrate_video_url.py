# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-13 08:17
from __future__ import unicode_literals
from urllib.parse import urlparse

from django.db import migrations


def video_url_to_id(video_url):
    return urlparse(video_url).path[1:]


def populate_video_id(apps, schema_editor):
    Talk = apps.get_model('speakers', 'Talk')
    for one in Talk.objects.all():
        if not one.video_url:
            continue
        one.video_id = video_url_to_id(one.video_url)
        one.save()


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0025_talk_video_id'),
    ]

    operations = [
        migrations.RunPython(populate_video_id),
    ]