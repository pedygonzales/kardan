from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from karfarma.choices import age_field, gender_field, degree_field, JOB_TYPES, salary_field, category_field, work_record


def home(request):
    posts = Post.objects.all().order_by('-post_date')[:5]
    context = {
        'age_field': age_field,
        'gender_field': gender_field,
        'degree_field': degree_field,
        'JOB_TYPES': JOB_TYPES,
        'salary_field': salary_field,
        'category_field': category_field,
        'work_record': work_record,
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by('-post_date')
        return context

    #login_url = 'login'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    #login_url = 'login'
    context_object_name = 'post'
