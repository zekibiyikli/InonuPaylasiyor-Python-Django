# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160423_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pay',
            name='dosya',
        ),
    ]
