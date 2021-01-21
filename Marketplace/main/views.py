from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')

# Create your views here.
