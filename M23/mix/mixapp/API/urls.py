from django.urls import path,include
# from mixapp.API.views import PartListAV, PartDetailAV, FullPartListAV,SellersListAV,CompanyListForGivenMPNAV,ExportCSVPARTAV
from mixapp.API.views import ExportCSVPARTAV



urlpatterns = [
    # path('partlist/', FullPartListAV.as_view(), name='part-full-list'),
    # path('list/<str:mpn>', PartListAV.as_view(), name='part-list'),
    #
    # path('<str:mpn>/', PartDetailAV.as_view(), name='part-detail'),
    #
    # path('sellerslist/', SellersListAV.as_view(), name='sellers-list'),
    # path('companylist/<str:mpn>', CompanyListForGivenMPNAV.as_view(), name='company-list'),
    path('export/', ExportCSVPARTAV.as_view(), name='export'),




]