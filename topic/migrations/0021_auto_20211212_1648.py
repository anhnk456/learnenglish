# Generated by Django 3.2.8 on 2021-12-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0020_alter_listening_sound'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listening',
            name='Sound',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newwords',
            name='Sound',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
    ]