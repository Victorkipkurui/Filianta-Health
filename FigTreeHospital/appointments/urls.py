from django.urls import path
from .views import book_appointment, appointment_list

urlpatterns = [
    path('book/', book_appointment, name='book_appointment'),
    path('appointments/', appointment_list, name='appointment_list'),
]
