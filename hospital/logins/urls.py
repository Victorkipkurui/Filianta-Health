from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path('signup/', user_views.sign_up, name='signup'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='logins/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('home',user_views.home, name ='home'),
    path('base',user_views.base, name ='base'),
]