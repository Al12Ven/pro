from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('movie/<int:pk>/', views.detail, name='detail'),
    path('movie/<int:pk>/review/', views.add_review, name='add_review'),
]