# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishGrade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='FrenchGrade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('pwd', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('english_word', models.CharField(max_length=200)),
                ('french_word', models.CharField(max_length=200)),
                ('english_grade', models.OneToOneField(to='words.EnglishGrade')),
                ('french_grade', models.OneToOneField(to='words.FrenchGrade')),
                ('user', models.ForeignKey(related_name='words', to='words.User')),
            ],
        ),
    ]
