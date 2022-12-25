# Generated by Django 4.0.5 on 2022-11-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubecmd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemapplication',
            name='build_instruction_json',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='systemapplication',
            name='build_instruction_yaml',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='systemapplication',
            name='config_text',
            field=models.TextField(null=True),
        ),
    ]