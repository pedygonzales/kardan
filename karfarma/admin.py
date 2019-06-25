from django.contrib import admin
from .models import Job, Karfarma
from django.http import HttpResponse
from django.core import serializers


def export_as_json(moodeladmin, request, queryset):
    response = HttpResponse(content_type='application/json')
    serializers.serialize('json', queryset, stream=response)
    return response


export_as_json.short_description = "خروجی اطلاعات به صورت فایل"


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['job_category', 'job_karfarma', 'job_title', 'job_skills',
                    'job_salary', 'job_limits', 'is_valid', 'job_type', 'job_age_limit', 'job_gender_limit', 'job_work_record', 'job_degree_limit']
    list_filter = ['job_category', 'job_karfarma', 'job_title',
                   'job_skills', 'job_salary', 'is_valid', 'job_type']
    actions = [export_as_json]
    #list_editable = ['job_title', 'job_skills', 'job_salary']


@admin.register(Karfarma)
class KarfarmaAdmin(admin.ModelAdmin):
    list_display = ['kfcname', 'kfmname', 'domain',
                    'address', 'kfmobile',  'is_registered']
    list_filter = ['kfcname', 'kfmname', 'domain',
                   'address', 'kfmobile',  'is_registered']
    actions = [export_as_json]
    #list_editable = ['kfcname', 'kfmname', 'domain', 'address', 'kfmobile']
