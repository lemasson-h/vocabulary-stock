# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20150731_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='english_word_description',
            field=models.TextField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='french_word_description',
            field=models.TextField(default=None, blank=True),
        ),
    ]
