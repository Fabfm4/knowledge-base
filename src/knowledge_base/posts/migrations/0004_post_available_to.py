# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-10 15:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_post_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='available_to',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
