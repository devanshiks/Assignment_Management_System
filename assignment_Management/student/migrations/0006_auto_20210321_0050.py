# Generated by Django 3.0.3 on 2021-03-20 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='submission_added_time',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='submission_marks',
        ),
    ]
