from rest_framework import serializers
from .models import Part, Manufacturer, MedianPrice1000, Company, Sellers, Prices, Offers




############### All Below serializers are for data insertion process. DON"T MAKE ANY CHANGE################################

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class MedianPrice1000Serializer(serializers.ModelSerializer):
    class Meta:
        model = MedianPrice1000
        fields = '__all__'


class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = '__all__'


class OffersSerializer(serializers.ModelSerializer):

    prices = PricesSerializer(many=True)
    class Meta:
        model = Offers
        fields = ['updated','prices','inventoryLevel']


class SellersSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    # company = CompanySerializer(many=True)

    offers = OffersSerializer(many=True)

    class Meta:
        model = Sellers
        # fields =
        fields = ['isAuthorized','company','offers']


class PartSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    medianPrice1000 = MedianPrice1000Serializer()
    sellers = SellersSerializer(many=True)


    class Meta:
        model = Part
        fields = ['estimatedFactoryLeadDays', 'totalAvail','mpn','manufacturer','medianPrice1000','sellers']
        lookup_field = "mpn"
        lookup_value_regex = "[^/]+"


    def create(self, validated_data):
        # print("validated_data at beginnng")
        # print(validated_data)
        manufacturer_data = validated_data.pop('manufacturer')
        medianPrice1000_data = validated_data.pop('medianPrice1000')
        sellers_data = validated_data.pop('sellers')
        part = Part.objects.create(**validated_data)
        Manufacturer.objects.create(part=part, **manufacturer_data)
        MedianPrice1000.objects.create(part=part, **medianPrice1000_data)
        sellers = Sellers.objects.create(part=part)
        sellers.save()
        totalCompnayCount = 0

        for seller_data in sellers_data:
            print("IS AUTHORISED")
            print(seller_data.get('isAuthorized'))
            setattr(sellers, 'isAuthorized', seller_data.get('isAuthorized'))
            sellers.save()

            Company.objects.create(part=part,sellers=sellers, **seller_data.get('company'))
            totalCompnayCount =totalCompnayCount +1


            offer_data = seller_data.get('offers')
            for offer in offer_data:
                print("Updated")
                print(offer['updated'])
                offers = Offers.objects.create(part=part,sellers=sellers, updated=offer['updated'],inventoryLevel=offer['inventoryLevel'])

                print(offer['prices'])
                for item in offer['prices']:
                    Prices.objects.create(part=part, offers=offers, **item)

        # Calculated field in model set below
        setattr(part, 'totalSellers', totalCompnayCount)
        part.save()

        return part








############### All Above serializers are for data insertion process. DON"T MAKE ANY CHANGE################################








# use beloew serialiser for showing only part list
class PartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'



# To get the value of a field:
#
# getattr(obj, 'field_name')
# To set the value of a field:
## setattr(obj, 'field_name', 'field value')
#
# ***Make sure to save obj after seting it shown below**
# setattr(sellers, 'isAuthorized', seller_data.get('isAuthorized'))
# sellers.save()
# To get all the fields and values for a Django object:
#
# [(field.name, getattr(obj,field.name)) for field in obj._meta.fields]
# You can read the documentation of Model _meta API which is really useful.