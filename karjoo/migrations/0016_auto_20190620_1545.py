# Generated by Django 2.2.2 on 2019-06-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karjoo', '0015_auto_20190618_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='karjoo',
            name='kjrequestjob',
            field=models.TextField(max_length=50, null=True, verbose_name='عنوان شغل درخواستی'),
        ),
        migrations.AddField(
            model_name='karjoo',
            name='kjworkrecord',
            field=models.CharField(choices=[('فاقد سابقه ', 'فاقد سابقه'), ('کمتر از یک سال', 'کمتر از یک سال'), ('یک تا سه سال', 'یک تا سه سال'), ('سه تا پنج سال', 'سه تا پنج سال'), ('بالاتر از پنج سال', 'بالاتر از پنج سال')], max_length=50, null=True, verbose_name='سابقه کاری'),
        ),
        migrations.AlterField(
            model_name='karjoo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='karjoo',
            name='transaction',
            field=models.CharField(blank=True, default=0, max_length=50, null=True, verbose_name='شماره تراکنش'),
        ),
    ]
