from django.shortcuts import render
from .models import Product,CategoryProduct,SaleMan,TagProduct


def home(request):
    turn_on_block = True
    return render(request, 'index.html', {'turn_on_block': turn_on_block})



from django.views.generic.list import ListView

class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = "main/product_list.html"

from django.views.generic.list import DetailView
class ProductDetail(DetailView):
    model = Product



# Create your views here.
