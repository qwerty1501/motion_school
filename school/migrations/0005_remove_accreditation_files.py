# Generated by Django 3.2.8 on 2022-05-26 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_accreditation_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accreditation',
            name='files',
        ),
    ]