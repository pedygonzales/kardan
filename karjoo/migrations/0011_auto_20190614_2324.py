# Generated by Django 2.2.2 on 2019-06-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karjoo', '0010_auto_20190614_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karjoo',
            name='kjgender',
            field=models.CharField(choices=[('مرد', 'مرد'), ('زن', 'زن'), ('فرقی ندارد', 'فرقی ندارد')], max_length=50, null=True, verbose_name='جنسیت'),
        ),
    ]