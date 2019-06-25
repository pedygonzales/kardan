from django.shortcuts import render, redirect
from .forms import KarjooRegisterForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Karjoo
from zeep import Client
from .choices import age_field, gender_field, degree_field, JOB_TYPES, salary_field, category_field, work_record
from karfarma.models import Job


def karjooregisterform(request):
    if request.method == 'POST':
        form = KarjooRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/karjoo')

    else:
        form = KarjooRegisterForm()
    return render(request, 'karjoo/karjoo_register.html', {'form': form})


def karjoohome(request):
    context = {
        'age_field': age_field,
        'gender_field': gender_field,
        'degree_field': degree_field,
        'JOB_TYPES': JOB_TYPES,
        'salary_field': salary_field,
        'category_field': category_field,
        'work_record': work_record,
    }
    return render(request, 'karjoo/karjoo.html', context)


class KarjooListView(ListView):
    model = Karjoo
    template_name = 'Karjoo/Karjoo_list.html'
    # login_url = 'login'


class KarjooDetailView(DetailView):
    model = Karjoo
    template_name = 'Karjoo/Karjoo_detail.html'
    # login_url = 'login'
    # context_object_name = 'Karjoo'


def job_search(request):
    queryset_list = Job.objects.all()
    if 'job_title' in request.GET:
        job_title = request.GET['job_title']
        if job_title:
            queryset_list = queryset_list.filter(
                job_title__icontains=job_title)

    if 'job_skills' in request.GET:
        job_skills = request.GET['job_skills']
        if job_skills:
            queryset_list = queryset_list.filter(
                job_skills__icontains=job_skills)

    if 'job_salary' in request.GET:
        job_salary = request.GET['job_salary']
        if job_salary:
            queryset_list = queryset_list.filter(
                job_salary__iexact=job_salary)
    if 'job_work_record' in request.GET:
        job_work_record = request.GET['job_work_record']
        if job_work_record:
            queryset_list = queryset_list.filter(
                job_work_record__iexact=job_work_record)

    if 'job_limits' in request.GET:
        job_limits = request.GET['job_limits']
        if job_limits:
            queryset_list = queryset_list.filter(
                job_limits__icontains=job_limits)

    if 'job_category' in request.GET:
        job_category = request.GET['job_category']
        if job_category:
            queryset_list = queryset_list.filter(
                job_category__iexact=job_category)

    if 'job_gender_limit' in request.GET:
        job_gender_limit = request.GET['job_gender_limit']
        if job_gender_limit:
            queryset_list = queryset_list.filter(
                job_gender_limit__iexact=job_gender_limit)

    if 'job_degree_limit' in request.GET:
        job_degree_limit = request.GET['job_degree_limit']
        if job_degree_limit:
            queryset_list = queryset_list.filter(
                job_degree_limit__iexact=job_degree_limit)

    if 'job_age_limit' in request.GET:
        job_age_limit = request.GET['job_age_limit']
        if job_age_limit:
            queryset_list = queryset_list.filter(
                job_age_limit__iexact=job_age_limit)

    context = {

        'jobs': queryset_list,
        'count': queryset_list.count(),
        'age_field': age_field,
        'gender_field': gender_field,
        'degree_field': degree_field,
        'JOB_TYPES': JOB_TYPES,
        'salary_field': salary_field,
        'category_field': category_field,
        'work_record': work_record,

    }
    return render(request, 'karjoo/job_search.html', context)


#

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/karjoo/verify/'


def send_request(request):
    result = client.service.PaymentRequest(
        MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(
            MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
