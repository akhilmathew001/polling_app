# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-21 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Author')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Blog')),
                ('tag_line', models.TextField(verbose_name='Tag line')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=250, verbose_name='HeadLine')),
                ('Blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Blog', verbose_name='Blog')),
                ('authors', models.ManyToManyField(to='polls.Author', verbose_name='Authors')),
            ],
        ),
    ]
