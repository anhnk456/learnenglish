# Generated by Django 3.2.8 on 2021-11-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sounds',
            name='Name',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
