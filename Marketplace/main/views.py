from django.shortcuts import render
from .models import Product,CategoryProduct,SaleMan,TagProduct
from django.views.generic.list import ListView
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UpdateProfileForm


def home(request):
    turn_on_block = True
    return render(request, 'index.html', {'turn_on_block': turn_on_block})





class ProductListView(ListView):
    model = Product
   # queryset = Product.objects.all()
    context_object_name = 'my_product'
    template_name = "main/product_list.html"
    paginate_by = 3

    def get_queryset(self, **kwargs):
        tag = self.request.GET.get('tag')
        if tag:
            return Product.objects.filter(tag_product__title_tag=tag)
        return super().get_queryset(**kwargs)

    def context_data(self, **kwargs):
        context = super(self).get_context_data(**kwargs)
        my_tag = self.request.GET.get('tag')
        if my_tag:
            context['tag'] = my_tag
        return context


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'main/product_detail.html'


class EditUserView(UpdateView):
    model = User
    form_class = UpdateProfileForm
    success_url = '/'
    template_name = 'update_profile.html'

        def get_object(self):
            return self.request.user

# Create your views here.
