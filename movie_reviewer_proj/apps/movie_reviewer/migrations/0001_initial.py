# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-27 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('lead_role_1', models.CharField(max_length=50)),
                ('lead_role_2', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('review', models.TextField(max_length=1500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]