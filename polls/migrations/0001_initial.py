# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('operation_text', models.CharField(max_length=100)),
                ('operation_date', models.DateField(verbose_name='date operation')),
                ('operation_summa', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
