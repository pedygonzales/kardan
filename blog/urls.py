from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("post_list/", views.PostListView.as_view(), name="post_list"),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

]
