# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20151120_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('in_or_out', models.BooleanField()),
                ('date', models.DateTimeField()),
                ('person_name', models.CharField(max_length=50)),
                ('book_name', models.CharField(max_length=100)),
                ('book_isbn', models.CharField(max_length=13)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='status',
        ),
        migrations.AddField(
            model_name='book',
            name='num_avaliable',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='num_total',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
