from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('time/', views.get_time, name='time'),
    path('comment/', views.get_comments, name='comments'),
    path('comment/save/', views.save_comment, name='save_comment'),
]