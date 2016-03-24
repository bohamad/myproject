# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160316_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statecapital',
            old_name='capital_population',
            new_name='population',
        ),
    ]
