from django.urls import path
from . import views as user_views

urlpatterns = [
    path('signup/', user_views.sign_up, name='signup'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('home/',user_views.home, name ='home'),
    path('index/',user_views.index, name ='index'),
    path('book-appointment/', user_views.book_appointment, name='appointment'),
    path('feedback/', user_views.feedback, name='feedback'),
]
 