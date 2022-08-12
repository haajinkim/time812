from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import GetProductsSerialziers
from .models import Product,UserProduct
# Create your views here.
import datetime

class ProductView(APIView):


    def get(self, request):


        all_products = Product.objects.all()

        return Response(GetProductsSerialziers(all_products, many=True).data,status=status.HTTP_200_OK)

    def post(self,request):

        product = request.data["product"]
        product = Product.objects.get(name=product)
        now = datetime.datetime.now().strftime ("%Y%m%d")
        end = datetime.datetime(days=365).strftime ("%Y%m%d") + datetime.datetime.now().strftime ("%Y%m%d")
        UserProduct.Create(
            user = request.user,
            product = product,
            statr_date = now,
            end_date = end
        )
        return Response(status=status.HTTP_200_OK)