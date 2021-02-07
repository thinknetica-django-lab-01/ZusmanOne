from django.shortcuts import render
from .models import Product,CategoryProduct,SaleMan,TagProduct
from django.contrib.auth.models import User,Group,Permission
from .forms import UpdateProfile
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

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


class ProductDetail(DetailView):
    model = Product
    template_name = 'main/product_detail.html'


class EditUserView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UpdateProfile
    success_url = '/'
    template_name = 'main/login_update.html'
    #login_url = '/accounts/profile'
    #redirect_field_name = '/login/'
    def get_object(self):
        return self.request.user

class ProductCreate(LoginRequiredMixin,CreateView):
    model = Product
    fields = '__all__'
    template_name = 'edit/product_form.html'


class ProductUpdate(LoginRequiredMixin,UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'edit/product_form.html'

class ProductDelete(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('goods')
    template_name = 'edit/product_delete.html'
    template_name_suffix = '_delete'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created,**kwargs):
    if created:
        common_users, created = Group.objects.get_or_create(name = 'common users')
        instance.groups.add(Group.objects.get(name='common users'))
