# Generated by Django 3.2 on 2021-04-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_rename_msg_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleve',
            name='username_elv',
            field=models.CharField(blank=True, db_column='USERNAME_ELV', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='username_ens',
            field=models.CharField(blank=True, db_column='USERNAME_ENS', max_length=255, null=True),
        ),
    ]