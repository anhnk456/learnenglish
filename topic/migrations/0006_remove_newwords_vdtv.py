# Generated by Django 3.2.8 on 2021-12-06 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0005_alter_newwords_vdtv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newwords',
            name='VdTV',
        ),
    ]
