# Generated by Django 3.2 on 2021-06-14 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messagge',
            new_name='message',
        ),
    ]
