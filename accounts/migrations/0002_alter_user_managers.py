# Generated by Django 4.0.4 on 2022-05-27 07:48

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
