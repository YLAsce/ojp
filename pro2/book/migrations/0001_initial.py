# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=13)),
                ('status', models.BooleanField(default=True)),
                ('press', models.CharField(max_length=100)),
            ],
        ),
    ]
