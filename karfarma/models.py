from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.contrib.auth.models import User
from .choices import degree_field, age_field, gender_field, JOB_TYPES, salary_field, category_field, work_record


class Karfarma(models.Model):
    kfcname = models.CharField(max_length=200, verbose_name='نام شرکت')
    kfmname = models.CharField(max_length=200, verbose_name='نام نماینده شرکت')
    domain = models.CharField(max_length=200, verbose_name='فیلد کاری')
    address = models.CharField(max_length=500, verbose_name='آدرس')
    kfmobile = models.CharField(max_length=200, verbose_name='شماره تماس')
    is_registered = models.BooleanField(default=False, verbose_name='ثبت شرکت')
    kfphoto = models.ImageField(
        upload_to='logo/', blank=True, verbose_name='لوگو')
    kfrtime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='نام کاربری سایت')

    class Meta:
        verbose_name = 'کارفرما'
        verbose_name_plural = 'کارفرمایان'

    def __str__(self):
        return self.kfcname


class Job(models.Model):
    job_category = models.CharField(
        null=True, blank=True, max_length=200, choices=category_field, verbose_name='دسته ی شغلی')
    job_title = models.CharField(
        max_length=200, verbose_name='عنوان اول شغل', blank=True, null=True)
    job_title2 = models.CharField(
        max_length=200, verbose_name='عنوان دوم شغل', blank=True, null=True)
    job_title3 = models.CharField(
        max_length=200, verbose_name='عنوان سوم شغل', blank=True, null=True)
    job_skills = models.TextField(verbose_name='مهارت های مورد نیاز')
    job_work_record = models.CharField(
        choices=work_record,  null=True, max_length=50, verbose_name='سابقه کاری')
    job_salary = models.CharField(
        null=True, max_length=200, choices=salary_field, verbose_name='حقوق')
    job_age_limit = models.CharField(
        choices=age_field, blank=True,  null=True, max_length=50, verbose_name='سن')
    job_gender_limit = models.CharField(
        choices=gender_field, blank=True,  null=True, max_length=50, verbose_name='جنسیت')
    job_degree_limit = models.CharField(
        choices=degree_field, blank=True,  null=True, max_length=100, verbose_name='مدرک تحصیلی')
    job_limits = models.TextField(verbose_name='محدودیت های شغل')
    is_valid = models.BooleanField(default=True, verbose_name='معتبراست')
    job_karfarma = models.ForeignKey(
        Karfarma, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='کارفرما')
    job_time = models.DateTimeField(auto_now=True)
    job_type = models.CharField(
        null=True, max_length=100, choices=JOB_TYPES, verbose_name='نوع شغل')

    class Meta:
        verbose_name = 'شغل'
        verbose_name_plural = 'شغل ها'

    def __str__(self):
        return self.job_title
