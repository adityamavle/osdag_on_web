from django.urls import path
from django.urls import include
from osdag.views import HomePage
urlpatterns = [
    path('', HomePage.as_view()),
]
