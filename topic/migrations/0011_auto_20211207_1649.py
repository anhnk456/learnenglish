# Generated by Django 3.2.8 on 2021-12-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0010_rename_exams_listening_cauhoi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaking',
            name='Exams',
        ),
        migrations.RemoveField(
            model_name='speaking',
            name='Sound',
        ),
        migrations.AddField(
            model_name='speaking',
            name='DapAn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]