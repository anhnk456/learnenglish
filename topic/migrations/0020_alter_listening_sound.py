# Generated by Django 3.2.8 on 2021-12-12 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0019_alter_newwords_sound'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listening',
            name='Sound',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
