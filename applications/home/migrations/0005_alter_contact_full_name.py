# Generated by Django 3.2 on 2021-06-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_home_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
    ]