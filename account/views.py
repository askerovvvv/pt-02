from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import CustomUser
from account.serializers import RegisterSerializer, UserListSerializer


# Create your views here.
class RegisterApiView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            message = (f"Пользователь успешно создан в "
                       f"нашей системе под никнеймом: {user.email}")
            return Response({"message": message}, status=201)
        return Response(serializer.errors, status=400)


class UserListApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer

"""
Сделать CRUD для user(через классы, функции) is_active
добавить пагинацию при получении пользователя
"""
