# Generated by Django 4.1.6 on 2023-03-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_rename_block_title_block_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='params',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='block',
            name='type',
            field=models.CharField(choices=[('table', 'Table'), ('text', 'Text')], default='text', max_length=200),
            preserve_default=False,
        ),
    ]
