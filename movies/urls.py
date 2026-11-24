from django.urls import path
from . import views

urlpatterns = [
    # Главная страница (список фильмов)
    path('', views.list, name='list'),
    
    # Страница конкретного фильма
    path('movie/<int:pk>/', views.detail, name='detail'),
    
    # Добавление отзыва (если используется отдельно)
    path('movie/<int:pk>/review/', views.add_review, name='add_review'),
]