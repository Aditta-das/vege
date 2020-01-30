from django.urls import path
from . import views
urlpatterns = [
    path('accounts/login', views.login, name='login'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/changepassword', views.change_password, name='change_password'),
    path('logout/', views.logout, name='logout'),
]