# Generated by Django 3.0.2 on 2020-02-06 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='znosubject',
            old_name='is_active_s',
            new_name='is_active_subject',
        ),
    ]
