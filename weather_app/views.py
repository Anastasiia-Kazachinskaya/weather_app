import os

import requests
from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv
from .models import People, Meta

load_dotenv()
key = 'a54b11f5c4a1ab993b8d3c85814491a0'
APPID = os.getenv(key)

def get_weather(request):
    city = request.POST.get('city', '')
    form = Meta(request.POST or None)
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'APPID': key,
        'lang': 'ru',
        'units': 'metric'
    }
    if form.is_valid():
        try:
            response = requests.get(url, params)
        except requests.ConnectionError as e:
            return HttpResponse(f'<сетевая ошибка - {e}>')
        if response.status_code == 451:
            return HttpResponse('<ошибка 451>')
        if response.status_code == 404:
            return HttpResponse('<ошибка 404>')
        if response.status_code == 200:
            weather = response.json()
            return render(request, 'index.html', {'weather': weather, 'form': form})
        else:
            return HttpResponse(response)
    else:
        form = Meta(request.POST)
        return render(request, 'index.html', {'form': form})


