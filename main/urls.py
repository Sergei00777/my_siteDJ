from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('skills/', views.skills, name='skills'),
    path('diplomas/', views.diplomas, name='diplomas'),
    path('contacts/', views.contacts, name='contacts'),
]