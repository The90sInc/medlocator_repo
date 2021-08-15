from django.urls import path
from . import views

urlpatterns = [
    path('become_pharmacy/', views.become_pharmacy, name='become_pharmacy'),
    #path('pharmacy-admin/', views.pharmacy_admin, name='pharmacy_admin')
]
