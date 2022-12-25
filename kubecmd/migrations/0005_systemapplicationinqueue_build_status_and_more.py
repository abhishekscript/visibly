# Generated by Django 4.0.5 on 2022-11-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubecmd', '0004_rename_config_json_systemapplication_config_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemapplicationinqueue',
            name='build_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Not Started'), (2, 'In Progress'), (3, 'Failed'), (4, 'Completed')], default=1),
        ),
        migrations.AlterField(
            model_name='systemapplicationinqueue',
            name='logs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='systemapplicationinqueue',
            name='reserved',
            field=models.BooleanField(default=True),
        ),
    ]