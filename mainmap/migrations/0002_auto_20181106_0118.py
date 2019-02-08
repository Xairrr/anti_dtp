# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 01:18
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmap', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dtp_area',
            options={'verbose_name': '\u041e\u0447\u0430\u0433 \u0414\u0422\u041f', 'verbose_name_plural': '\u041e\u0447\u0430\u0433\u0438 \u0414\u0422\u041f'},
        ),
        migrations.AddField(
            model_name='dtp_card',
            name='Correct',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dtp_area',
            name='Description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='dtp_area',
            name='Factors',
            field=models.TextField(null=True, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0441\u043e\u043f\u0443\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0444\u0430\u043a\u0442\u043e\u0440\u044b'),
        ),
        migrations.AlterField(
            model_name='dtp_area',
            name='Main_types',
            field=models.TextField(null=True, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0432\u0438\u0434\u044b \u0414\u0422\u041f \u043d\u0430 \u0443\u0447\u0430\u0441\u0442\u043a\u0435'),
        ),
        migrations.AlterField(
            model_name='dtp_area',
            name='Name',
            field=models.TextField(verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0447\u0430\u0441\u0442\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='dtp_area',
            name='Nar',
            field=models.TextField(null=True, verbose_name='\u041d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u044f \u0441\u0445\u0435\u043c\u044b \u0434\u043e\u0440\u043e\u0436\u043d\u043e\u0433\u043e \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='dtp_area',
            name='Queries',
            field=models.TextField(null=True, verbose_name='\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043e\u0431\u0449\u0435\u043d\u0438\u044f \u0441 \u0432\u043b\u0430\u0441\u0442\u044f\u043c\u0438'),
        ),
        migrations.AlterField(
            model_name='dtp_area',
            name='Solutions',
            field=models.TextField(null=True, verbose_name='\u041f\u0440\u0435\u0434\u043f\u043e\u043b\u0430\u0433\u0430\u0435\u043c\u044b\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='dtp_area',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(help_text='\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u0438\u043a\u043e\u043d\u043a\u0443 \u0441 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043e\u043c \u0438\u043b\u0438 \u043f\u044f\u0442\u0438\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c, \u0447\u0442\u043e\u0431\u044b \u043d\u0430\u0447\u0430\u0442\u044c \u043e\u0442\u0440\u0438\u0441\u043e\u0432\u043a\u0443 \u0443\u0447\u0430\u0441\u0442\u043a\u0430', srid=4326, verbose_name='\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
    ]