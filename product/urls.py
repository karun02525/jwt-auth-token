from django.urls import path
from .views import ProductAPI,RegisterUser

urlpatterns = [
    path('products',ProductAPI.as_view(), name='Products'),
    path('register',RegisterUser.as_view(), name='Register'),
    
    
    
]
    # path('product',product, name='product'),
    # path('products',products,name='product'),
    # path('add-product',add_product,name='Add Product'),
    # path('update-product/<id>',update_product,name='Update Product'),
    # path('delete-product/<id>',delete_product,name='Delete Product'),
    # path('get-book',get_books,name='Get Book'),

