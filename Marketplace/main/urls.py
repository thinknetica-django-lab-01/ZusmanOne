from django.urls import path
from . import views
from .views import EditUserView

urlpatterns = [
    path('goods/', views.ProductListView.as_view(), name='goods'),
    path('good/<int:pk>', views.ProductDetail.as_view(), name ='good-detail'),
    path('accounts/profile/', EditUserView.as_view(), name = 'update-profile'),
]

urlpatterns += [    #тут хранятся маршруты для создания удаления изменения
    path(r'goods/create/', views.ProductCreate.as_view(), name='goods-create'),
    path(r'good/<int:pk>/update/', views.ProductUpdate.as_view(), name='good-update'),
    path(r'^good/<int:pk>/delete/', views.ProductDelete.as_view(), name='good-delete'),


]