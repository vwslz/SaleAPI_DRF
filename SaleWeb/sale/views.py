from django.shortcuts import render

# Create your views here.

# from sale.models import SKU
# from sale.serializers import SKUSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# def SKUList(APIView):
#     def get(self, request, format=None):
#         sku = SKU.objects.all()
#         serializer = SKUSerializer(sku, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SKUSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class SKUDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return SKU.objects.get(pk=pk)
#         except SKU.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         sale = self.get_object(pk)
#         serializer = SKUSerializer(sale)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         sku = self.get_object(pk)
#         serializer = SKUSerializer(sku, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         sku = self.get_object(pk)
#         sku.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from sale.models import SKU
from sale.serializers import SKUSerializer
from rest_framework import generics

class SKUList(generics.ListCreateAPIView):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer

class SKUDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer