# Generated by Django 2.2 on 2022-04-29 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220429_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='jobseeker_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
