# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161022_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='war_participated',
        ),
    ]
