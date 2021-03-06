# Generated by Django 3.2 on 2021-04-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_auto_20210418_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_admin', models.CharField(blank=True, db_column='USERNAME_ADMIN', max_length=255, null=True, unique=True)),
                ('nom_admin', models.CharField(blank=True, db_column='NOM_ADMIN', max_length=255, null=True)),
                ('pwd_admin', models.CharField(blank=True, db_column='PWD_ADMIN', max_length=255, null=True)),
                ('date_nai_admin', models.DateField(blank=True, db_column='DATE_NAI_ADMIN', null=True)),
            ],
            options={
                'db_table': 'ADMIN',
                'managed': True,
            },
        ),
    ]
