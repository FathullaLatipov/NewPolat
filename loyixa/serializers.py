from rest_framework import serializers
from .models import Zapchast, Maxsulot, Order


class ZapchastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zapchast
        fields = ('id', 'name_uz', 'name_ru', 'image')

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)


class MaxsulotSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()
    brand_img_url = serializers.SerializerMethodField()

    class Meta:
        model = Maxsulot
        fields = ('zapchast', 'name_uz', 'name_ru', 'description', 'description_ru', 'price', 'brand',
                  'brand_image', 'image', 'status', 'img_url', 'brand_img_url')

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)

    def get_brand_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.brand_image.url)


class Maxsulot2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Maxsulot
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    maxsulot = Maxsulot2Serializer()

    class Meta:
        model = Order
        fields = '__all__'
