# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('grade', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=11)),
                ('student_id', models.CharField(max_length=11)),
                ('class_id', models.CharField(max_length=11)),
                ('school', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('passwd', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=30)),
                ('reason', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='contestant',
            name='team',
            field=models.ForeignKey(to='wincap.Team'),
        ),
    ]
