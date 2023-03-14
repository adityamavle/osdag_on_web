from django.shortcuts import render, redirect
from django.utils.html import escape, urlencode
from django.http import HttpResponse
from django.views import View
# Create your views here.

class HomePage(View):
    def get(self, request):
        return render(request, 'osdag/homepage.html')