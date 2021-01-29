from django.urls import path
from . import views

urlpatterns = [
    path('goods/', views.ProductListViews.as_view(), name='goods'),
]