# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-25 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200, verbose_name='Token')),
                ('expires', models.IntegerField(verbose_name='过期时间')),
            ],
        ),
        migrations.CreateModel(
            name='JsapiTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=200, verbose_name='Ticket')),
                ('expires', models.IntegerField(verbose_name='过期时间')),
            ],
        ),
    ]
