from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About World")

def login(request):
    emailAddress = request.GET.get('loginEmail', 'No Email Address Written')
    password = request.GET.get('loginPassword', 'No Password Written')
    print(f"User entered {emailAddress} , {password}")

    return render(request, 'login.html')

def jokes(request):
    print("Inside def")

    if request.method == 'POST':

        getJokesBtn = request.POST.get('showJokes', 'on')
        print("Got btn value")
        if getJokesBtn == "on":
            limit = request.POST.get('jokesLimit')
            response = requests.get(f"https://v2.jokeapi.dev/joke/Dark?blacklistFlags=nsfw&amount={limit}")
            print(response)
            if response.status_code == 200:
                data = response.json()
                print(data)
                return render(request, 'jokes.html', {'jokesData': data} )

    
    return render(request, 'jokes.html')