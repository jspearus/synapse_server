from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard.html', {})

def home(request):
    return render(request, 'home.html', {})

def remote(request):
    return render(request, 'remote.html', {})


def term(request, room_name):
    return render(request, 'term.html', {
        'room_name': room_name
    })
