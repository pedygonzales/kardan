from django.contrib import admin
from .models import Karjoo
from django.http import HttpResponse
from django.core import serializers


def export_as_json(moodeladmin, request, queryset):
    response = HttpResponse(content_type='application/json')
    serializers.serialize('json', queryset, stream=response)
    return response


export_as_json.short_description = "خروجی اطلاعات به صورت فایل"


@admin.register(Karjoo)
class KarjooAdmin(admin.ModelAdmin):
    list_display = ['kjname', 'kjfamily', 'kjtahsilat', 'kjage',
                    'kjmaharat', 'kjsalary', 'kjgender', 'kjmelli', 'address', 'kjmobile', 'is_registered', 'kjmaghta', 'transaction']
    list_filter = ['kjmaghta', 'kjsalary', 'kjtahsilat',
                   'kjmaharat', 'kjage',  'is_registered']
    actions = [export_as_json]
