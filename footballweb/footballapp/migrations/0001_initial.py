# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('League_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='Match Date')),
                ('result', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('player_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('team_name', models.CharField(max_length=200)),
                ('league', models.ForeignKey(to='footballapp.League')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='footballapp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(to='footballapp.Team', related_name='team1'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(to='footballapp.Team', related_name='team2'),
        ),
    ]
