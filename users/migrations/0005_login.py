# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-07 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_adhaar_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.BigIntegerField()),
                ('pc', models.IntegerField()),
            ],
        ),
    ]