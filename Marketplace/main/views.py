from django.shortcuts import render
from .models import Product,CategoryProduct,SaleMan,TagProduct
from django.views.generic.list import ListView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    turn_on_block = True
    return render(request, 'index.html', {'turn_on_block': turn_on_block})





class ProductListView(ListView):
    model = Product
   # queryset = Product.objects.all()
    context_object_name = 'my_product'
    template_name = "main/product_list.html"
    paginate_by = 3
    # def get_context_data(self, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     if not context.get('is_paginated', False):
    #         return context
    #
    #     paginator = context.get('paginator')
    #     num_pages = paginator.num_pages
    #     current_page = context.get('page_obj')
    #     page_no = current_page.number
    #
    #     if num_pages <= 5 or page_no <= 3:  # case 1 and 2
    #         pages = [x for x in range(1, min(num_pages + 1, 6))]
    #     elif page_no > num_pages - 3:  # case 4
    #         pages = [x for x in range(num_pages - 5, num_pages + 1)]
    #     else:  # case 3
    #         pages = [x for x in range(page_no - 4, page_no + 1)]
    #
    #     context.update({'pages': pages})
    #     return context


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'main/product_detail.html'



# Create your views here.
