# Generated by Django 3.2 on 2021-06-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210629_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='phone'),
        ),
    ]