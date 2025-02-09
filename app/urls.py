from django.urls import path

from app import views

urlpatterns = [
    path('create/game/', views.create_game),
    path('get/games/', views.get_games),
    path('get/game/<int:id>/', views.get_game_by_id),
    path('update/game/<int:id>/', views.update_game),
    path('delete/game/<int:id>/', views.delete_game),
    path('test/', views.create_random_number),
    path('game/create/', views.CreateGameApiView.as_view()),
    path('game/list/', views.GameListApiView.as_view()),
    path('game/retrieve/<pk>', views.GameRetrieveApiView.as_view()),
    path('category/list/create', views.CategoryListCreateAPIView.as_view()),
]