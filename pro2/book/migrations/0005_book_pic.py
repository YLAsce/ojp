# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20151120_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pic',
            field=models.ImageField(default=b'pics/None/no-img.jpg', upload_to=b'pics/'),
        ),
    ]
