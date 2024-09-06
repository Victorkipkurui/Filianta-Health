from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path('signup/', user_views.sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='logins/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('home/',user_views.home, name ='home'),
    path('index/',user_views.index, name ='index'),
    path('book-appointment/', user_views.book_appointment, name='appointment'),
]
   