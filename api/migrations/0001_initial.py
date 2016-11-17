# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_body', models.TextField()),
                ('morpheme', models.TextField()),
                ('content_scored', models.TextField()),
                ('admin_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
