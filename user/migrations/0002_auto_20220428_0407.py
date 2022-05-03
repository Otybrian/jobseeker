# Generated by Django 2.2 on 2022-04-28 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='name',
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='skills',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employer',
            name='company_bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='employer',
            name='company_location',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employer',
            name='company_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employer',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
