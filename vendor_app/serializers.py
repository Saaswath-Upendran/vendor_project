from rest_framework.serializers import ModelSerializer
from .models import *


class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor_Model
        fields = "__all__"


class PurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = Purchase_Order_Model
        fields = "__all__"

class HistoricalPerformanceSerializer(ModelSerializer):
    class Meta:
        model = Historical_Performance_Model
        fields = "__all__"



