from django.urls import path
from .views import *


urlpatterns=[
    path('register/',RegisterApiView.as_view(), name='Register' ),
    path('login/', loginview, name='Login'),
    path('story/',StoryApiView.as_view(), name='Story'),
]