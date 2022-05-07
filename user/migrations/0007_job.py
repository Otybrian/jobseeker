# Generated by Django 2.2 on 2022-05-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_jobseeker_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=255)),
                ('requirements', models.TextField()),
                ('jobtype', models.TextField(choices=[('Part Time', 'Part-Time'), ('Remote', 'Remote'), ('Full Time', 'Full-Time')], max_length=30)),
            ],
        ),
    ]
