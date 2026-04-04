from django.urls import path

from . import views


app_name = 'heroes'

urlpatterns = [
    path('', views.show_form, name='show-form'),
    path('success/', views.show_success, name='show-success')
]
