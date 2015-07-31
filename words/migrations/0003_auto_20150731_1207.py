# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='englishgrade',
            name='count_failed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='englishgrade',
            name='count_succeed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='englishgrade',
            name='grade',
            field=models.DecimalField(default=Decimal('0'), max_digits=20, decimal_places=2),
        ),
        migrations.AddField(
            model_name='frenchgrade',
            name='count_failed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frenchgrade',
            name='count_succeed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frenchgrade',
            name='grade',
            field=models.DecimalField(default=Decimal('0'), max_digits=20, decimal_places=2),
        ),
        migrations.AddField(
            model_name='word',
            name='english_word_description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='word',
            name='french_word_description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(verbose_name='Username (email)', default='email@email.com', unique=True, max_length=255),
        ),
    ]
