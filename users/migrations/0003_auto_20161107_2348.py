# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-07 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_adhaar'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.BigIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='adhaar',
            name='uid',
            field=models.BigIntegerField(unique=True),
        ),
    ]
