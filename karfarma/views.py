from django.shortcuts import render
from .forms import KarfarmaRegisterForm, KarfarmaAddJobForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Job
from karjoo.models import Karjoo
from .choices import age_field, gender_field, degree_field, JOB_TYPES, salary_field, category_field, work_record


def karfarmaregisterform(request):
    if request.method == 'POST':
        form = KarfarmaRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = KarfarmaRegisterForm()
    return render(request, 'karfarma/karfarma_register.html', {'form': form})


def karfarmahome(request):
    context = {
        'age_field': age_field,
        'gender_field': gender_field,
        'degree_field': degree_field,
        'JOB_TYPES': JOB_TYPES,
        'salary_field': salary_field,
        'category_field': category_field,
        'work_record': work_record,
    }
    return render(request, 'karfarma/karfarma.html', context)


def karfarmaaddjobform(request):
    if request.method == 'POST':
        form = KarfarmaAddJobForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/karfarma/add_job')

    else:
        form = KarfarmaAddJobForm()
    return render(request, 'karfarma/add_job.html', {'form': form})


class JobListView(ListView):
    model = Job
    template_name = 'karfarma/job_list.html'
    #login_url = 'login'


class JobDetailView(DetailView):
    model = Job
    template_name = 'karfarma/job_detail.html'
    #login_url = 'login'
    #context_object_name = 'Karjoo'


def skill_search(request):
    queryset_list = Karjoo.objects.all()
    if 'kjmaharat' in request.GET:
        kjmaharat = request.GET['kjmaharat']
        if kjmaharat:
            queryset_list = queryset_list.filter(
                kjmaharat__icontains=kjmaharat)

    if 'kjmaghta' in request.GET:
        kjmaghta = request.GET['kjmaghta']
        if kjmaghta:
            queryset_list = queryset_list.filter(
                kjmaghta__iexact=kjmaghta)
    if 'kjworkrecord' in request.GET:
        kjworkrecord = request.GET['kjworkrecord']
        if kjworkrecord:
            queryset_list = queryset_list.filter(
                kjworkrecord__iexact=kjworkrecord)

    if 'kjtahsilat' in request.GET:
        kjtahsilat = request.GET['kjtahsilat']
        if kjtahsilat:
            queryset_list = queryset_list.filter(
                kjtahsilat__icontains=kjtahsilat)
    if 'kjrequestjob' in request.GET:
        kjrequestjob = request.GET['kjrequestjob']
        if kjrequestjob:
            queryset_list = queryset_list.filter(
                kjrequestjob__icontains=kjrequestjob)

    if 'kjage' in request.GET:
        kjage = request.GET['kjage']
        if kjage:
            queryset_list = queryset_list.filter(
                kjage__iexact=kjage)

    if 'kjsalary' in request.GET:
        kjsalary = request.GET['kjsalary']
        if kjsalary:
            queryset_list = queryset_list.filter(
                kjsalary__iexact=kjsalary)

    if 'kjgender' in request.GET:
        kjgender = request.GET['kjgender']
        if kjgender:
            queryset_list = queryset_list.filter(
                kjgender__iexact=kjgender)

    context = {
        'karjoos': queryset_list,
        'count': queryset_list.count(),
        'age_field': age_field,
        'gender_field': gender_field,
        'degree_field': degree_field,
        'JOB_TYPES': JOB_TYPES,
        'salary_field': salary_field,
        'category_field': category_field,
        'work_record': work_record,
    }
    return render(request, 'karfarma/skill_search.html', context)
