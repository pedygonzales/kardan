# Generated by Django 2.2.1 on 2019-06-01 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karfarma', '0004_auto_20190530_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='karfarma',
            name='job_opportunity',
        ),
        migrations.AddField(
            model_name='job',
            name='job_karfarma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='karfarma.Karfarma', verbose_name='کارفرما'),
        ),
    ]
