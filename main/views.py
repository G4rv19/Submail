from django.shortcuts import render

def tasklist(request):
    return render(request, 'home.html')
