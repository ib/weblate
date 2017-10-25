# -*- coding: utf-8 -*-
# Generated by Django 1.11.5.dev20170816164241 on 2017-10-25 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20170605_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='user_agent',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='activity',
            field=models.CharField(choices=[('auth-connect', 'auth-connect'), ('auth-disconnect', 'auth-disconnect'), ('connect', 'connect'), ('failed-auth', 'failed-auth'), ('locked', 'locked'), ('login', 'login'), ('password', 'password'), ('register', 'register'), ('removed', 'removed'), ('reset', 'reset'), ('reset-request', 'reset-request'), ('tos', 'tos')], db_index=True, max_length=20),
        ),
    ]
