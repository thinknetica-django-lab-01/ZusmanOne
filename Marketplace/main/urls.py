from django.urls import path
from . import views
from .views import EditUserView

urlpatterns = [
    path('goods/', views.ProductListView.as_view(), name='goods'),
    path(r'^goods/<int:pk>', views.ProductDetail.as_view(), name ='good-detail'),
    path('accounts/profile/', EditUserView.as_view(), name = 'update-profile'),
]