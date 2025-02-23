from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from account.views import RegisterApiView, UserListApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('user/list/', UserListApiView.as_view()),
]



