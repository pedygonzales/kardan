# Generated by Django 2.2.1 on 2019-06-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karjoo', '0002_auto_20190530_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karjoo',
            name='kjresume',
            field=models.FileField(blank=True, upload_to='resume/', verbose_name='رزومه '),
        ),
    ]