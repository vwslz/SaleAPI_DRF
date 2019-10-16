from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from sale import views
from sale.views import ProductViewSet, CustomerViewSet, BuyViewSet, api_root

'''
Using rounter
'''

router = DefaultRouter()

router.register(r'product', ProductViewSet)
router.register(r'cart', BuyViewSet)
router.register(r'customer', CustomerViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('home', views.home),
    # path('login', LoginView.as_view(), name="user_login"),
    path('api-auth/', include('rest_framework.urls'))
]

'''
Using path
'''
from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from sale.views import ProductViewSet, CustomerViewSet, BuyViewSet, api_root
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
# buy_list = BuyViewSet.as_view({
#     'get': 'list',
#     # 'post': 'create'
# })
# buy_detail = BuyViewSet.as_view({
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
#     path('buy/', buy_list, name='buy-list'),
#     path('buy/<int:pk>/', buy_detail, name='buy-detail'),
#     path('api-auth/', include('rest_framework.urls')),
# ])