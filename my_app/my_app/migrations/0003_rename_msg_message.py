# Generated by Django 3.2 on 2021-04-17 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_rename_message_msg'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Msg',
            new_name='Message',
        ),
    ]
