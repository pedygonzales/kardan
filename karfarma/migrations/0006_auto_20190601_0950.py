# Generated by Django 2.2.1 on 2019-06-01 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karfarma', '0005_auto_20190601_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('پاره وقت', 'پاره وقت'), ('تمام وقت', 'تمام وقت'), ('پروژه ای', 'پروژه ای')], max_length=100, null=True),
        ),
    ]
