from django.shortcuts import render
from django.contrib.auth.models import User, Group

# Create your views here.
def home(request):
    import requests
    import json

    # Grab coronavirus Data
    api_request = requests.get("https://covid19-japan-web-api.now.sh/api//v1/prefectures")
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api': api})

