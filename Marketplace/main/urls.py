from django.urls import path
from . import views

urlpatterns = [
    path('goods/', views.ProductListView.as_view(), name='goods'),
    path('goods/<int:pk>', views.ProductDetail.as_view(), name ='goods-detail')
]