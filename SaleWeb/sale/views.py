from django.shortcuts import render, redirect

# Create your views here.
from idna import unicode
from rest_framework.renderers import TemplateHTMLRenderer

from sale.models import Product, Cart, Customer
from sale.serializers import ProductSerializer, CustomerSerializer, CartSerializer
from rest_framework import permissions, generics
from sale.permissions import IsOwnerOrReadOnly, IsBuyerOrReadOnly
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response

# @login_required
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_root(request, format=None):

    return Response({
        'users': reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'buy': reverse('buy-list', request=request, format=format)
    })

'''
Custom Pages
'''
def home(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    numbers = [1,2,3,4,5]
    products = Product.objects.all()
    args = {
        'user': user,
        'products': products,
        'numbers' : numbers,
    }

    return render(request, 'sale/home.html', args)

'''
Additional functions
'''
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/account')
#     else:
#         form = RegistrationForm
#         args = {'form': form}
#         return render(request, 'sale/ ')

'''
view set
'''
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # permissions.IsAdminUser,
    ]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsBuyerOrReadOnly,
    ]

    @action(detail=False, methods=['get'], serializer_class=CartSerializer,
            url_path='customer/(?P<customer_id>[^/.]+)', name='customer-cart')
    def customer_cart(self, request, customer_id, pk=None):
        buyer = Customer.objects.all()[(int)(customer_id)-1]
        cartitems = Cart.objects.all().filter(buyer=buyer)
        # cartitems = Cart.objects.all()
        serializer = self.get_serializer(cartitems, many=True)
        return Response(serializer.data)