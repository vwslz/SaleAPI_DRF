from django.urls import path
from sale import views

urlpatterns = [
    path('sale/', views.SKU_list),
    path('sale/<int:pk>/', views.SKU_detail),
]