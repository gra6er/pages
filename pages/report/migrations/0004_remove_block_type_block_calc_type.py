# Generated by Django 4.1.6 on 2023-03-31 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_block_params_block_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='type',
        ),
        migrations.AddField(
            model_name='block',
            name='calc_type',
            field=models.CharField(choices=[('CryptoTicker', 'CryptoTicker'), ('PlainText', 'PlainText')], default='PlainText', max_length=200),
            preserve_default=False,
        ),
    ]