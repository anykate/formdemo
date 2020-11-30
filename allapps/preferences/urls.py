from django.urls import path
from . import views

app_name = 'preferences'

urlpatterns = [
    path('add/', views.IndexView.as_view(), name='add-preferences'),
]
