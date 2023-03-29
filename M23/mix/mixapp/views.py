from mixapp models import DataSource,MPN,Seller,Price_QTY
from pdapp.api.serializers import (DataSourceSerializer,Price_QTYSerializer,MPNSerializer,SellerSerializer)
from rest_framework import generics


class MPNListAV(generics.ListCreateAPIView):
    serializer_class = MPNSerializer
    queryset = MPN.objects.all()

class MPNDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = MPN.objects.all()
    serializer_class = MPNSerializer

