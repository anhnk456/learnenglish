# Generated by Django 3.2.8 on 2021-12-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0006_remove_newwords_vdtv'),
    ]

    operations = [
        migrations.AddField(
            model_name='newwords',
            name='VdTV',
            field=models.CharField(default=0, max_length=255),
        ),
    ]