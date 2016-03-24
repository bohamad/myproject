# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160315_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='mane',
        ),
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
