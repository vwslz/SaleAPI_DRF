# from django.urls import path

# from django.urls import path
# from django.urls import re_path
# from rest_framework.urlpatterns import format_suffix_patterns
# from sale import views
# from django.conf.urls import include
#
# urlpatterns = [
#     path('', views.api_root),
#     path('sale/', views.SKUList.as_view(), name='sku-list'),
#     path('sale/<int:pk>/', views.SKUDetail.as_view(), name='sku-detail'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-retail'),
#     path('api-auth/', include('rest_framework.urls')),
#     path('', views.api_root),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sale import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'skus', views.SKUViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]