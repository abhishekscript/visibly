# Generated by Django 4.0.5 on 2022-11-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubecmd', '0005_systemapplicationinqueue_build_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemapplication',
            name='extra_config',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='systemapplicationinqueue',
            name='instruction_yaml',
            field=models.TextField(null=True),
        ),
    ]
