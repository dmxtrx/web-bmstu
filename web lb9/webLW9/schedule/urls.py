from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schedule/', views.index, name='schedule'),
    path('update-schedule/', views.update_schedule, name='update_schedule'),]