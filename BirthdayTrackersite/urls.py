from django.urls import path
from BirthdayTrackersite import views

urlpatterns = [
    path('', views.birthday, name='birthday'),
    path('success/', views.success, name='success'),

]