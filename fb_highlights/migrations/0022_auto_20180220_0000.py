# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-20 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb_highlights', '0021_auto_20180219_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlightnotificationstat',
            name='send_time',
            field=models.DateTimeField(),
        ),
    ]
