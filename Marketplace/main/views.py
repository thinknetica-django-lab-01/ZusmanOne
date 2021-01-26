from django.shortcuts import render

def home(request):
    turn_on_block = False
    return render(request, 'index.html', {'turn_on_block': turn_on_block})



# Create your views here.
