from django.urls import path

from app import views

urlpatterns = [
    path('create/game/', views.create_game),
    path('get/games/', views.get_games),
    path('get/game/<int:id>/', views.get_game_by_id),
    path('update/game/<int:id>/', views.update_game),
]