from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from sale import views
from sale.views import ProductViewSet, CustomerViewSet, CartViewSet, api_root

'''
Using rounter
'''

router = DefaultRouter()

router.register(r'product', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'customer', CustomerViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # for Fun
    path('home', views.home),
]

'''
Using path
'''
from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from sale.views import ProductViewSet, CustomerViewSet, CartViewSet, api_root
from sale import views

# product_list = ProductViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# product_detail = ProductViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# customer_list = CustomerViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# customer_detail = CustomerViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy'
# })
# cart_list = CartViewSet.as_view({
#     'get': 'list',
#     # 'post': 'create'
# })
# cart_detail = CartViewSet.as_view({
#     'get': 'retrieve',
#     # 'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('home', views.home),
#     path('product/', product_list, name='product-list'),
#     path('product/<int:pk>/', product_detail, name='product-detail'),
#     path('user/', customer_list, name='user-list'),
#     path('user/<int:pk>/', customer_detail, name='user-detail'),
#     path('cart/', buy_list, name='cart-list'),
#     path('cart/<int:pk>/', cart_detail, name='cart-detail'),
#     path('api-auth/', include('rest_framework.urls')),
# ])