# Generated by Django 3.2.8 on 2021-12-07 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0015_alter_newwords_sound'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newwords',
            name='Sound',
        ),
    ]
