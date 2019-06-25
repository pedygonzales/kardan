from django.urls import path
from . import views


urlpatterns = [
    path('', views.karfarmahome, name='karfarma_home'),
    path('search/', views.skill_search, name='skill_search'),
    path('karfarma_register', views.karfarmaregisterform,
         name='karfarma_register'),
    path('add_job/', views.karfarmaaddjobform, name='add_job'),
    path("job_list/", views.JobListView.as_view(), name="job_list"),
    path('<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
]
