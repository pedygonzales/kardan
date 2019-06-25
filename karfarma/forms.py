from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select
from .models import Job, Karfarma


class KarfarmaRegisterForm(ModelForm):
    class Meta:
        model = Karfarma
        fields = [
            'kfcname', 'kfmname', 'domain', 'address', 'kfmobile', 'kfphoto', 'user'
        ]


class KarfarmaAddJobForm(ModelForm):
    class Meta:
        model = Job
        fields = [
            'job_category', 'job_title', 'job_title2', 'job_title3', 'job_skills', 'job_work_record', 'job_salary', 'job_age_limit', 'job_gender_limit', 'job_degree_limit', 'job_limits', 'job_type', 'job_karfarma'
        ]
        widgets = {
            'job_skills': Textarea(attrs={'cols': 21, 'rows': 10}),
            'job_limits': Textarea(attrs={'cols': 21, 'rows': 10}),
            'job_salary': Select(attrs={'cols': 21, 'rows': 10}),
            'job_category': Select(),
        }
