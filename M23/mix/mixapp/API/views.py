from django.db.models import Q
from mixapp.models import Part,Sellers,Company,MedianPrice1000,Sellers,Manufacturer,Offers,Prices
from mixapp.serializers import (PartSerializer,SellersSerializer,OffersSerializer,PricesSerializer,CompanySerializer,ManufacturerSerializer,MedianPrice1000Serializer,PartListSerializer)
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly



import csv
from django.http import HttpResponse



class ExportCSVPARTAV(APIView):
    print("start")
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        print("level1")

        writer = csv.writer(response)
        writer.writerow(["MPN", "Estimated-Factory-Lead-Days", "Total-Avail","Median-Currency", "Median-Price", "Median-Quantity","Manufacturer","Inventory-Level","Last Updated"])

        # print("ARGS")
        # print(self.kwargs)
        pricesset = Prices.objects.all()
        row =[]

        for pr in pricesset:
            # print("prices loop")
            iprice = pr.price
            iquantity = pr.quantity
            icurrency = pr.currency
            offerssetid= Prices.objects.filter(id=pr.id).values('offers__id').first()['offers__id']

            print("offerssetid")
            print(offerssetid)
            offersset = Offers.objects.filter(id=offerssetid)
            companysetid = offerssetid
            if Company.objects.filter(id=companysetid).exists():
                companyset = Company.objects.filter(id=companysetid)
                print(companyset[0].name)
                companyname = companyset[0].name




            for o in offersset:
                # print("offers-loop")
                inventoryLevel = o.inventoryLevel
                updated = o.updated
                sellerssetid =Offers.objects.filter(id=o.id).values('sellers__id').first()['sellers__id']
                sellersset = Sellers.objects.filter(id=sellerssetid)
                row = row + [companyname, inventoryLevel , updated]

                for s in sellersset:
                    # print("sellers-loop")
                    partsetid = Sellers.objects.filter(id=s.id).values('part__id').first()['part__id']
                    partset = Part.objects.filter(id=partsetid)
                    m = MedianPrice1000.objects.filter(id=s.id)
                    mnf =Manufacturer.objects.filter(id=s.id)
                    mprice = m[0].price
                    mquantity = m[0].quantity
                    mcurrency = m[0].currency
                    mnfname = mnf[0].name
                    # print("mprice in s loop")
                    # print(mprice)
                    row = [mcurrency,mprice,mquantity,mnfname] + row

                    for p in partset:
                        # print("part-loop")
                        row = [p.mpn, p.estimatedFactoryLeadDays, p.totalAvail] + row

                        row = row + [iprice, iquantity, icurrency]
                        print(row)
                        print("\n")
                        writer.writerow(row)
                        row = []


        return response


#
# #################################################################################################################
#
# # read queryset in dataframe
#
#
# ##############################################################################################################
#
#
# # For path('<str:mpn>/', PartDetailAV.as_view(), name='part-detail')
# # Do I need this? as same can be done with PartDetailList with one sku
# class PartDetailAV(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PartSerializer
#     queryset = Part.objects.all()
#     def get_object(self,**kwargs):
#         queryset = self.get_queryset()
#         print(queryset)
#         print("ARGS")
#         print(self.kwargs)
#         queryset = queryset.filter(mpn=self.kwargs['mpn'])
#         print("FILTERED")
#         print(queryset)
#         return queryset.first()
#
# ##############################################################################################################
#
# # For path('list/<str:mpn>', PartListAV.as_view(), name='part-list'),
# # https://stackoverflow.com/questions/20222457/django-building-a-queryset-with-q-objects
# # https://stackoverflow.com/questions/3929278/what-does-ior-do-in-python
# class PartListAV(generics.ListCreateAPIView):
#     serializer_class = PartSerializer
#
#     def get_queryset(self):
#
#         mpnstring = self.kwargs['mpn']
#         print(mpnstring)
#         mpnlist = []
#         mpnlist.append(mpnstring.split(','))
#         print("array")
#         mpndata = mpnlist[0]
#         q_objects = Q()  # Create an empty Q object to start with
#         for t in mpndata:
#             q_objects |= Q(mpn=t)  # 'or' the Q objects together
#         return Part.objects.filter(q_objects)
#
#
# #####################################################################################################
#
# # Fro     path('fulllist/', FullPartListAV.as_view(), name='part-full-list')
# # show only part list without any more details
# class FullPartListAV(generics.ListCreateAPIView):
#     serializer_class = PartListSerializer
#     queryset = Part.objects.all()
#
#
# #########################################################################################################
#
# class SellersListAV(generics.ListCreateAPIView):
#     serializer_class = SellersSerializer
#     queryset = Sellers.objects.all()
#
#     def get_queryset(self):
#         queryset = Sellers.objects.all()
#
#
#
#
# #######################################################################################
#
#
#
# class CompanyListForGivenMPNAV(generics.ListCreateAPIView):
#     serializer_class = CompanySerializer
#
#     def get_queryset(self):
#         mpnstring = self.kwargs['mpn']
#         print(mpnstring)
#         mpnlist = []
#         mpnlist.append(mpnstring.split(','))
#         print("array")
#         mpndata = mpnlist[0]
#         q_objects = Q()  # Create an empty Q object to start with
#         for t in mpndata:
#             # q_objects |= Q(mpn=t)  # 'or' the Q objects together
#             q_objects |= Q(sellers__part__mpn=t)
#         return Company.objects.filter(q_objects)
#
#
# ###########################################################################################
#
