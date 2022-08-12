from rest_framework import serializers
from .models import Product



class GetProductsSerialziers(serializers.ModelSerializer):

    all_product = serializers.SerializerMethodField()

    def get_all_product(self,obj):

        if obj.is_active == True:

            return obj.name, obj.desc, obj.price


    class Meta:
        model =  Product
        fields = ["all_product"]