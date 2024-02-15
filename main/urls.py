from django.urls import path
from . import views 
from .views import email_view

urlpatterns = [
    path('', views.tasklist, name='tasks'),
    path('email/', email_view, name='email_view'),
]