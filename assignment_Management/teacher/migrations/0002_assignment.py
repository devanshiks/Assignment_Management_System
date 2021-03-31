# Generated by Django 3.0.3 on 2021-03-17 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_student'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('assignment_name', models.CharField(max_length=50)),
                ('assignment_created', models.DateTimeField()),
                ('assignment_due_date', models.DateTimeField()),
                ('assignment_file', models.FileField(null=True, upload_to='files/')),
                ('assignment_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Course')),
                ('assignment_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Teacher')),
            ],
        ),
    ]
