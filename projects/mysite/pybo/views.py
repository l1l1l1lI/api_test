import requests
from django.shortcuts import render


def index(request):
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        response.raise_for_status()
        data = response.json()
        print(data)
    except requests.RequestException as e:
        print(e)
    return render(request, 'dd.html', {'data': data})


def search(request):
    print('hi')
    if request.method == 'POST':
        keyword = request.POST['query']
        print(keyword)
