# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='answer_number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ForeignKey(editable=False, to='qa.Image'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='index_1',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='index_2',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='score',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(editable=False, to='qa.User'),
        ),
    ]
