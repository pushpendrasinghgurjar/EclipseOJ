# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 09:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 9, 22, 57, 857721, tzinfo=utc)),
        ),
    ]
