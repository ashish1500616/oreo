# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_login_user_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_1_a',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_1_b',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_3_a',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_3_b',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_two_a',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_two_b',
            field=models.URLField(blank=True),
        ),
    ]