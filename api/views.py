from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializer import *


# Create your views here.


class RegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()

    serializer_class = RegisterSerializer


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def loginview(request):
    email=request.data.get('email')
    password=request.data.get('password')
    verify=authenticate(email=email, password=password)

    if verify is None:
        return Response({'Invalid':'Check your email or password'}, status=400)
    else:
        refresh=RefreshToken.for_user(verify)
        return Response({
            'user':str(email),
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=200)

