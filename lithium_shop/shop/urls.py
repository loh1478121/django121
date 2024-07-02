from django.urls import path
from .views import ProductListCreate, CustomUserDetail

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('users/<int:pk>/', CustomUserDetail.as_view(), name='customuser'),
]
