# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-11-17 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_app', '0005_auto_20221117_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='letters_info',
        ),
        migrations.AddField(
            model_name='letterinfo',
            name='subscriber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing_app.Subscriber'),
        ),
    ]
