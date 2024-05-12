from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductsListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsByMenuAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        menu_id = self.kwargs['menu_id']
        return Product.objects.filter(menu_id=menu_id)
