# Generated by Django 3.0.7 on 2020-06-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0002_bug_is_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='bug_number',
            field=models.IntegerField(default=0),
        ),
    ]