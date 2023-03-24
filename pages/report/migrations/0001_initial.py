# Generated by Django 4.1.6 on 2023-02-08 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_title', models.CharField(max_length=200)),
                ('gen_time', models.DateTimeField(verbose_name='datetime generated')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=200)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.report')),
            ],
        ),
    ]