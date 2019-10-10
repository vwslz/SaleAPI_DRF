# from django.urls import path
# from sale import views
#
# urlpatterns = [
#     path('sale/', views.SKUList),
#     path('sale/<int:pk>/', views.SKUDetail),
# ]


from django.urls import path
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from sale import views

urlpatterns = [
    path('sale/', views.SKUList.as_view()),
    path('sale/<int:pk>/', views.SKUDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)