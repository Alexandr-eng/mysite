# Create your views here.
from rest_framework import viewsets

from shop.models import User, Category, Warehouse, Product
from shop.serializers import ApiUserSerializer, CategorySerializer, \
    WarhouseSerializer, ProductSerializer


# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['post', 'path', 'get']
    serializer_class = ApiUserSerializer

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def __str__(self):
        return self.name

class WarhouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarhouseSerializer

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
