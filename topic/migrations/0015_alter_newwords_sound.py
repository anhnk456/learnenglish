# Generated by Django 3.2.8 on 2021-12-07 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0005_alter_sounds_link'),
        ('topic', '0014_alter_newwords_sound'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newwords',
            name='Sound',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sounds.sounds'),
        ),
    ]
