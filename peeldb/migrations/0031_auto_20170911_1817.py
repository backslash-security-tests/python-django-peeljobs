# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-11 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peeldb', '0030_auto_20170904_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencyresume',
            name='mobile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
