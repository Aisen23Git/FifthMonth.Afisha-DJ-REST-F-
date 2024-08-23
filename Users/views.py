# from django.shortcuts import render
from  rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserAuthSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['POST'])
def auth_api_view(request):
    serializer = UserAuthSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data('username')
    password = serializer.validated_data('password')

    user = authenticate(usernmae = username, password = password)
    if user is not None:
        token_, created = Token.objects.get_or_create(user=user)
        return Response(data = {'key': token_.key})
    return Response(status = status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def register_api_view(request):
    serializer = UserRegisterSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.create_user(username = username, password = password, is_active = False )
    #create Code / email/ until date
    return Response(data = {'user_id': user.id}, status = 201)