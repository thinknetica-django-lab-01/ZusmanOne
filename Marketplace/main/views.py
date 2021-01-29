from django.shortcuts import render


def home(request):
    turn_on_block = True
    return render(request, 'index.html', {'turn_on_block': turn_on_block})



from django.views import generic

class ProductListView(generic.ListView):
    model = Product



# Create your views here.
