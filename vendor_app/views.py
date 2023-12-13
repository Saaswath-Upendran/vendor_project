from django.shortcuts import render
from .serializers import *
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404,HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date
from django.db.models import Count, Avg
# Create your views here.


class CreateUser(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self,request,format='json'):

        pass


class VendorView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def get_object(self, pk):
        try:
            return Vendor_Model.objects.get(pk=pk)
        except Vendor_Model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format="json"):
        snippet = self.get_object(pk)
        serializer = VendorSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format="json"):
        snippet = self.get_object(pk)
        serializer = VendorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format="json"):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class VendorListView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def get(self, request, format="json"):
        snippets = Vendor_Model.objects.all()
        serializer = VendorSerializer(snippets, many=True)
        return Response(serializer.data)
    

    def post(self,request,format="json"):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class Purchase_OrderView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def get_object(self, pk):
        try:
            return Purchase_Order_Model.objects.get(pk=pk)
        except Purchase_Order_Model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format="json"):
        snippet = self.get_object(pk)
        serializer = PurchaseOrderSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format="json"):
        snippet = self.get_object(pk)
        serializer = PurchaseOrderSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format="json"):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class Purchase_OrderListView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def get(self, request, format="json"):
        snippets = Vendor_Model.objects.all()
        serializer = VendorSerializer(snippets, many=True)
        return Response(serializer.data)
    

    def post(self,request,format="json"):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


def calculate_and_save_performance(id):
    vendor = Vendor_Model.objects.get(id=id)  # Replace 1 with the vendor ID
    dated_on = date.today()  # Replace this with the date you want to use

    # On-Time Delivery Rate
    completed_pos = Purchase_Order_Model.objects.filter(status='completed')
    completed_pos_delivered_on_time = completed_pos.filter(delivery_date__lte=date).count()
    on_time_delivery_rate = completed_pos_delivered_on_time / completed_pos.count()

    # Quality Rating Average
    quality_rating_average = Purchase_Order_Model.objects.filter(quality_rating__isnull=False).aggregate(Avg('quality_rating'))

    # Average Response Time
    average_response_time = Purchase_Order_Model.objects.filter(acknowledgment_date__isnull=False).aggregate(Avg('acknowledgment_date' - 'issue_date'))

    # Fulfilment Rate
    fulfilled_pos = Purchase_Order_Model.objects.filter(status='completed', issues__isnull=True)
    fulfilment_rate = fulfilled_pos.count() / Purchase_Order_Model.objects.count()

    # historical_performance = Historical_Performance_Model(
    #     vendor=vendor,
    #     date=dated_on,
    #     on_time_delivery_rate=on_time_delivery_rate,
    #     quality_rating_avg=quality_rating_average['quality_rating__avg'],
    #     average_response_time=average_response_time['acknowledgment_date__avg'] - average_response_time['issue_date__avg'],
    #     fulfillment_rate=fulfilment_rate
    # )
    # historical_performance.save()

    return vendor,dated_on,on_time_delivery_rate,quality_rating_average['quality_rating__avg'],average_response_time,fulfilment_rate
class PerformanceByVendorView(APIView):
    """
    This class returns a list of performance metrics for each vendor.
    It also allows adding new entries by making POST requests.
    The URL pattern for this view is `api/vendors/metrics/`
    """
    @staticmethod
    def get(request, format=None):
        vendors = Vendor_Model.objects.all().order_by('name')
        serializer = HistoricalPerformanceSerializer(vendors, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        '''
        Adds a new entry in the table. Used when making a POST request to `api/vendors/metrics/`
        '''
        serializer = HistoricalPerformanceSerializer(data=request.DATA)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            id = serializer.validated_data['vendor']
            metric = calculate_and_save_performance(id)
            serialized_metric = HistoricalPerformanceSerializer(metric)
            return Response(serialized_metric.data)
        # Views related to individual metrics (not the summary)
        #     def retrieve_metric(self, request, pk, format=None):
        #         try:
        #             metric = VendorMetric_Detail.objects.get(pk=pk)
        #         except VendorMetric_Detail.DoesNotExist:
        #             return HttpResponse(status=404)
        #         serializer = MetricRetrieveUpdateDestroySerializer(metric)
        #         return Response(serializer.f fullSerialize(metric))
        #     def update_metric(self, request, pk):
        #         try:
        #             metric = VendorMetric_Detail.objects.get(pk=pk)
        #         except VendorMetric_Detail.DoesNotExist:
        #              return HttpResponsenot_found)
        #         serializer = MetricRetrieveUpdateDestroySerializer(metric,
        #                                                           data=request.DATA,
        #                                                           context={'request': request})
        #         if serializer.is_valid():
        #             serializer.save()
        #             return Response(serializer.data)
        #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
  