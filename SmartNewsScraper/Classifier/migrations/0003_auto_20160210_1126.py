# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-10 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classifier', '0002_auto_20160209_1919'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Synonyms',
            new_name='Synonym',
        ),
    ]
