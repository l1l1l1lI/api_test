# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("..")
from django.contrib.sites import requests
from django.shortcuts import render

def index(request):
    return render(request, 'dd.html', {})


