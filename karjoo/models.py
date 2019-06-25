from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from .choices import age_field, gender_field, degree_field, salary_field, work_record


class Karjoo(models.Model):
    kjname = models.CharField(max_length=200, verbose_name='نام کارجو')
    kjfamily = models.CharField(
        max_length=200, verbose_name='نام خانوادگی کارجو')
    kjage = models.CharField(
        choices=age_field,  null=True, max_length=50, verbose_name='سن')
    kjsalary = models.CharField(
        choices=salary_field,  null=True, max_length=120, verbose_name='حقوق درخواستی')
    kjgender = models.CharField(
        choices=gender_field,  null=True, max_length=50, verbose_name='جنسیت')
    kjworkrecord = models.CharField(
        choices=work_record,  null=True, max_length=50, verbose_name='سابقه کاری')
    kjrequestjob = models.TextField(
        null=True, max_length=50, verbose_name='عنوان شغل درخواستی')
    email = models.EmailField(null=True, blank=True,
                              max_length=254, verbose_name='ایمیل')
    kjphoto = models.ImageField(
        upload_to='avatars/', blank=True, verbose_name='عکس ')
    kjmelli = models.CharField(max_length=200, verbose_name='شماره ملی')
    address = models.TextField(max_length=500, verbose_name='آدرس')
    kjmobile = models.CharField(max_length=200, verbose_name='شماره تماس')
    kjmaghta = models.CharField(blank=True, null=True,
                                choices=degree_field, max_length=50, verbose_name='مدرک دانشگاهی')
    kjtahsilat = models.TextField(
        blank=True, null=True, verbose_name='رشته دانشگاهی')
    kjmaharat = models.TextField(verbose_name='مهارتها')
    is_registered = models.BooleanField(
        default=False, verbose_name='کاربر ثبت شده ')
    kjresume = models.FileField(
        upload_to='resume/', blank=True, verbose_name='رزومه ')
    kjtime = models.DateTimeField(auto_now=True)
    kjrating = models.IntegerField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='نام کاربری سایت')
    transaction = models.CharField(null=True, blank=True,
                                   max_length=50, default=0, verbose_name='شماره تراکنش')

    class Meta:
        verbose_name = 'کارجو'
        verbose_name_plural = 'کارجویان'

    def __str__(self):
        return self.kjname
