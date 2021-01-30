from django.urls import path
from . import views

urlpatterns = [
    path('goods/', views.ProductListView.as_view(), name='goods'),
    path(r'^goods/<int:pk>', views.ProductDetail.as_view(), name ='good-detail'),
]