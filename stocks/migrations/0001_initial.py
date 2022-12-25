# Generated by Django 4.0.5 on 2022-06-26 16:44

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=common.models.tz_now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('security_id', models.CharField(max_length=50)),
                ('security_code', models.IntegerField(db_index=True, unique=True)),
                ('security_name', models.CharField(max_length=100)),
                ('issuer_name', models.CharField(max_length=100)),
                ('status', models.PositiveSmallIntegerField(choices=[('ACTIVE', 1), ('IN_ACTIVE', 0), ('SUSPENDED', 2), ('DELISTED', 3)])),
                ('group', models.PositiveSmallIntegerField(choices=[('IP', 3), ('B', 2), ('ZP', 12), ('MT', 5), ('M', 4), ('X', 9), ('Z', 11), ('T', 8), ('P', 6), ('R', 7), ('A', 1), ('XT', 10)])),
                ('face_value', models.FloatField()),
                ('industry', models.CharField(max_length=50)),
                ('sector_name', models.CharField(max_length=50)),
                ('group_name', models.CharField(max_length=50)),
                ('sub_group_name', models.CharField(max_length=50)),
                ('isin_number', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
