from glob import translate

from django.db.transaction import commit
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.template.context_processors import request
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
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
    if request.data.get('email')=="" or request.data.get('password')=="":
        return Response({'Null':'Please enter all the required fields to login'}, status=400)
    else:
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

class StoryApiView(generics.ListCreateAPIView:
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


