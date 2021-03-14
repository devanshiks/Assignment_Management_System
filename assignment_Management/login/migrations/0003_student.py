# Generated by Django 3.0.3 on 2021-03-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stu_email', models.CharField(help_text='write your email', max_length=50, primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=30)),
                ('stu_dob', models.DateTimeField()),
                ('stu_gender', models.CharField(max_length=10)),
                ('stu_sem', models.IntegerField()),
                ('stu_branch', models.CharField(max_length=6)),
                ('stu_address', models.CharField(help_text='write your add', max_length=100)),
                ('stu_city', models.CharField(max_length=20)),
                ('stu_state', models.CharField(max_length=20)),
                ('stu_zip', models.CharField(max_length=6)),
                ('stu_mobile_no', models.CharField(max_length=10)),
                ('stu_image', models.ImageField(blank=True, upload_to='stu_pics')),
            ],
        ),
    ]
