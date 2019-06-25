from django.urls import path, include
from .views import karjooregisterform
from . import views

urlpatterns = [
    path('', views.karjoohome, name='karjoo_home'),
    path('pay/', include('payment.urls')),
    path('search/', views.job_search, name='job_search'),
    path('karjoo_register', karjooregisterform, name='karjoo_register'),
    path("karjoo_list/", views.KarjooListView.as_view(), name="karjoo_list"),
    path('<int:pk>/', views.KarjooDetailView.as_view(), name='karjoo_detail'),
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
]
