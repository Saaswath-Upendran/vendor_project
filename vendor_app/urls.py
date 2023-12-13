from django.urls import path
from .views import *

app_name = "vendor_app"

urlpatterns = [
    path("vendors",VendorListView.as_view(),name="vendors_list_create"),
    path("vendors/<int:pk>/",VendorView.as_view(),name="vendors_view"),
    path("purchase_orders/<int:pk>/",Purchase_OrderView.as_view(),name="purchase_view"),
    path("purchase_orders",Purchase_OrderListView.as_view(),name="purchase_orders_create"),
    path("vendors/<int:pk>/performance",PerformanceByVendorView.as_view(),name="performance"),
    path("logout",LogoutAndBlacklistRefreshTokenForUserView.as_view(),name="logout"),
]