from django.contrib import admin
from django.urls import path
from home.views import CategoryAPIView, ManufacturerAPIView, ProductAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories', CategoryAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category_detail'),
    path('manufacturers', ManufacturerAPIView.as_view(), name='manufacturer_list'),
    path('manufacturers/<int:pk>/', ManufacturerAPIView.as_view(), name='manufacturer_detail'),
    path('products', ProductAPIView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product_detail'),
]
