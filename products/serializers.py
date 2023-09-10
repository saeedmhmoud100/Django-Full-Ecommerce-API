from rest_framework import serializers

from products.models import Image, Color, Product


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True,required=False)
    class Meta:
        model = Product
        fields = '__all__'
