# Generated by Django 2.2.2 on 2019-06-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karjoo', '0012_auto_20190617_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='karjoo',
            name='transaction',
            field=models.CharField(default=0, max_length=50, verbose_name=0),
        ),
    ]