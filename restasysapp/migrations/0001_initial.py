# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mesa_id', models.ForeignKey(to='restasysapp.Mesa')),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos_Fechados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pedidos_id', models.ForeignKey(to='restasysapp.Pedidos')),
            ],
        ),
        migrations.CreateModel(
            name='Pratos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ingredientes', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='pedidos',
            name='pratos_id',
            field=models.ForeignKey(to='restasysapp.Pratos'),
        ),
    ]
