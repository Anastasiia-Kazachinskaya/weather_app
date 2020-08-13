import requests
from .env import API_KEY
from django.shortcuts import render
from dotenv import load_dotenv
from .models import People, Meta
load_dotenv()


def get_weather(request):
    city = request.POST.get('city','')
    url = 'http://api.openweathermap.org/data/2.5/weather'
    if form.is_valid():
        response = request.get(url, city , API_KEY)
    else:
        form = Meta(request.POST)
        return render_to_response('new_stmt.html', {'form': form, }, context_instance=RequestContext(request))


