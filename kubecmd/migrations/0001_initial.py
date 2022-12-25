# Generated by Django 4.0.5 on 2022-11-15 20:11

import common.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=common.models.tz_now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('version', models.FloatField(default=0.1)),
                ('build_instruction_json', models.JSONField(null=True)),
                ('build_instruction_yaml', models.TextField(null=True)),
                ('build_status', models.PositiveSmallIntegerField(choices=[(1, 'Not Started'), (2, 'In Progress'), (3, 'Failed'), (4, 'Completed')], default=True)),
                ('config_json', models.JSONField(null=True)),
                ('config_text', models.JSONField(null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('name', 'version')},
            },
        ),
        migrations.CreateModel(
            name='SystemApplicationInQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=common.models.tz_now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('reserved', models.BooleanField(default=False)),
                ('app_type', models.CharField(choices=[('mysql_5_7', 'Mysql 5 7'), ('wordpress_6_0', 'Wordpress 6 0')], db_index=True, max_length=30)),
                ('instruction_json', models.JSONField(null=True)),
                ('instruction_yaml', models.JSONField(null=True)),
                ('instruction_text', models.TextField(null=True)),
                ('system_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kubecmd.systemapplication')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystemApplicationConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=common.models.tz_now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('config', models.JSONField()),
                ('config_text', models.TextField()),
                ('system_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kubecmd.systemapplication')),
            ],
            options={
                'unique_together': {('system_application', 'name')},
            },
        ),
    ]
