from django.db import models
import uuid
from simple_history.models import HistoricalRecords


class Part(models.Model):

    estimatedFactoryLeadDays = models.IntegerField(blank=True, null=True)
    mpn = models.CharField(max_length=255, blank=True, null=True)
    totalAvail = models.IntegerField(blank=True, null=True)
    totalSellers = models.IntegerField(blank=True,null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.mpn)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    part = models.OneToOneField(Part, on_delete=models.CASCADE, blank=True,related_name='manufacturer',null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.name)



        # # "medianPrice1000": {
        #     "currency": "USD",
        #     "price": 2.8425849999999997,
        #     "quantity": 1000
        # }


class MedianPrice1000(models.Model):
    currency = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    part = models.OneToOneField(Part, on_delete=models.CASCADE,related_name='medianPrice1000',null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.dbId)



class Sellers(models.Model):
    isAuthorized = models.BooleanField(blank=True, null=True)
    # wheneven unique constraint fails change it to Foreign key
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name='sellers',null=True)
    # part = models.ManyToManyField(Part,related_name='sellers',null=True)

    history = HistoricalRecords()

    def __str__(self):
        return str(self.dbId)




class Company(models.Model):
    homepageUrl = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    # sellers = models.ManyToManyField(Sellers, blank=True,related_name='company_sellers')
    #Many to one Relationship https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
    sellers = models.ForeignKey(Sellers, blank=True, related_name='company',on_delete=models.CASCADE,null=True)

    ###############
    part = models.ForeignKey(Part,related_name='company_part',null=True,on_delete=models.CASCADE)
    ##################
    history = HistoricalRecords()

    def __str__(self):
        return str(self.name)


class Offers(models.Model):
    updated = models.DateTimeField(blank=True, null=True)
    inventoryLevel = models.IntegerField(blank=True, null=True)
    sellers = models.ForeignKey(Sellers, blank=True,related_name='offers',null=True,on_delete=models.CASCADE)
    part = models.ForeignKey(Part,related_name='offers_part',null=True,on_delete=models.CASCADE)

    history = HistoricalRecords()

    def __str__(self):
        return str(self.sellers)


class Prices(models.Model):
    currency = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    offers = models.ForeignKey(Offers, blank=True, null=True, on_delete=models.CASCADE,related_name='prices')
    part = models.ForeignKey(Part,related_name='prices_part',null=True,on_delete=models.CASCADE)

    history = HistoricalRecords()

    def __str__(self):
        return str(self.Offers)




