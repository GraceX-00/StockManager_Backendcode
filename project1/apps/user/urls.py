# urls.py

from django.urls import path

from user.views import login

urlpatterns = [
    path('login/', login, name='login'),
]

