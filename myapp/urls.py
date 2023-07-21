from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.product_list, name='product_list'),
    path('product/<int:product_id>/',views.productDetails,name='product'),
    path('cart/',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    # path('contact',views.contact,name='contact'),
    path('update_item/',views.updatItem,name="update_item"),
    path('process_order/',views.processOrder,name="processOrder")
]
