# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-16 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('higherguidanceforum', '0002_teachers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='higherguidanceforum.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sluf', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='higherguidanceforum.UserProfile')),
                ('subjects', models.ManyToManyField(related_name='studying_students', to='higherguidanceforum.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Forums',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='higherguidanceforum.UserProfile')),
                ('subjects', models.ManyToManyField(related_name='teachers', to='higherguidanceforum.Subject')),
            ],
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='category',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='higherguidanceforum.SubjectForum'),
        ),
    ]
