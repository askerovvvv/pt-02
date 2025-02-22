from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import RegisterSerializer


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