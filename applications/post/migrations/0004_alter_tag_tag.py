# Generated by Django 3.2 on 2021-07-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210630_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=50, verbose_name='Tag'),
        ),
    ]