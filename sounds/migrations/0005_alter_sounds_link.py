# Generated by Django 3.2.8 on 2021-12-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0004_alter_sounds_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sounds',
            name='Link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
