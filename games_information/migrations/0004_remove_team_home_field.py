# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 16:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0003_team_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='home_field',
        ),
    ]