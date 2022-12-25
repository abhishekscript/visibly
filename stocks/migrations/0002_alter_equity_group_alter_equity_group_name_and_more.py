# Generated by Django 4.0.5 on 2022-06-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equity',
            name='group',
            field=models.PositiveSmallIntegerField(choices=[('A', 1), ('B', 2), ('IP', 3), ('M', 4), ('MT', 5), ('P', 6), ('R', 7), ('T', 8), ('X', 9), ('XT', 10), ('Z', 11), ('ZP', 12)]),
        ),
        migrations.AlterField(
            model_name='equity',
            name='group_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equity',
            name='industry',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equity',
            name='sector_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equity',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[('IN_ACTIVE', 0), ('ACTIVE', 1), ('SUSPENDED', 2), ('DELISTED', 3)]),
        ),
        migrations.AlterField(
            model_name='equity',
            name='sub_group_name',
            field=models.CharField(max_length=100),
        ),
    ]