from django.urls import path
from django.contrib.auth.views import LogoutView 
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('book_seat/<int:film_id>/', views.book_seat, name='book_seat'),
    path('movies/', views.movie_list, name='movie_list'),
    path('book_seat/<int:film_id>/', views.book_seat, name='book_seat'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'), 
   ] 