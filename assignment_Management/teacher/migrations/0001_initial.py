# Generated by Django 3.0.3 on 2021-03-16 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=30)),
                ('course_branch', models.CharField(max_length=50)),
                ('course_credit', models.DecimalField(decimal_places=2, max_digits=5)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Teacher')),
            ],
        ),
    ]
