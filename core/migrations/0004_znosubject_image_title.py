# Generated by Django 3.0.3 on 2020-02-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200207_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='znosubject',
            name='image_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
