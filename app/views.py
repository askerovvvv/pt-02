from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response

from app.models import GameInformation, Category
from app.serializers import GameInfoSerializer, TestSerializer, CategorySerializer


# Create your views here.

@api_view(["POST"])
def create_game(request):
    serializer = GameInfoSerializer(data=request.data)
    if serializer.is_valid():
        game = serializer.save()
        return Response({
            "name": game.name,
            "price": game.price,
            "version": game.version,
            "date_issue": game.date_issue,
            "company_name": game.company_name,
            "id": game.id,
            "created_at": game.created_at
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_games(request):
    games = GameInformation.objects.all()
    serializer = GameInfoSerializer(games, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_game_by_id(request, id):
    game = GameInformation.objects.filter(id=id).first()
    if not game:
        return Response({"message": "Game Not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = GameInfoSerializer(game)
    return Response(serializer.data)


@api_view(["PUT"])
def update_game(request, id):
    game = GameInformation.objects.filter(id=id).first()
    if not game:
        return Response({"message": "Game Not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = GameInfoSerializer(game, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_game(request, id):
    game = GameInformation.objects.filter(id=id).first()
    if not game:
        return Response({"message": "Game Not found"}, status=status.HTTP_404_NOT_FOUND)
    game.delete()
    return Response({"message": "deleted!"}, status=status.HTTP_200_OK)

import random

@api_view(["POST"])
def create_random_number(request):
    print(request.data)
    serializer = TestSerializer(data=request.data)
    if serializer.is_valid():
        num1 = serializer.data.get("num1")
        num2 = serializer.data.get("num2")
        if num1 > num2:
            return Response({"message": "nelzya"}, status=400)
        return Response({"number:": random.randint(num1, num2)}, status=200)
    return Response("", status=500)


class CreateGameApiView(CreateAPIView):
    queryset = GameInformation.objects.all()
    serializer_class = GameInfoSerializer



class GameListApiView(ListAPIView):
    queryset = GameInformation.objects.all()
    serializer_class = GameInfoSerializer


class GameRetrieveApiView(RetrieveAPIView):
    queryset = GameInformation.objects.all()
    serializer_class = GameInfoSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
