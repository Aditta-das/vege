from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('details/<int:details_id>', views.details, name='details'),
    path('details/<int:details_id>/comment', views.details, name='details'),
]
