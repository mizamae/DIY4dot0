# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='custom_perm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('view_devices', 'Can see available devices'), ('change_state', 'Can change the state of the devices'), ('add_device', 'Can add new devices to the installation'), ('add_report', 'Can configure and add reports'), ('view_report', 'Can view reports configured'), ('view_plots', 'Can see the historic plots from any device')),
            },
        ),
    ]
