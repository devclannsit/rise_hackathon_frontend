# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-07 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adhaar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=3)),
                ('yob', models.IntegerField()),
                ('dep', models.CharField(max_length=100)),
                ('lm', models.CharField(max_length=20)),
                ('loc', models.CharField(max_length=100)),
                ('vtc', models.CharField(max_length=100)),
                ('po', models.CharField(max_length=100)),
                ('dist', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
                ('pc', models.IntegerField()),
            ],
        ),
    ]