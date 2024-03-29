# Generated by Django 2.2.1 on 2019-05-29 13:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Karjoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kjname', models.CharField(max_length=200, verbose_name='نام کارجو')),
                ('kjfamily', models.CharField(max_length=200, verbose_name='نام خانوادگی کارجو')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('kjphoto', models.ImageField(blank=True, upload_to='avatars/')),
                ('kjmelli', models.CharField(max_length=200, verbose_name='شماره ملی')),
                ('address', models.TextField(max_length=500, verbose_name='آدرس')),
                ('kjmobile', models.CharField(max_length=200, verbose_name='شماره تماس')),
                ('kjtahsilat', models.TextField(verbose_name='تحصیلات')),
                ('kjmaharat', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None), size=None, verbose_name='مهارتها ')),
                ('is_registered', models.BooleanField(default=False)),
                ('kjresume', models.FileField(blank=True, upload_to='resume/')),
                ('kjtime', models.DateTimeField(auto_now_add=True)),
                ('kjrating', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'کارجو',
                'verbose_name_plural': 'کارجویان',
            },
        ),
    ]
