from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'assignment2_application-home'),
    path('about/', views.about, name = 'assignment2_application-about'),
    path('countries/', views.countries, name = 'assignment2_application-countries' )
]