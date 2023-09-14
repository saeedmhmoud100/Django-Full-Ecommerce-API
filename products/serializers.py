from django.contrib.auth import get_user_model
from rest_framework import serializers

from brands.models import Brand
from brands.serializers import BrandSerializer
from categories.models import Category
from categories.serializers import CategorySerializer
from products.models import Image, Color, Product


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id','name']


class ProductSerializer(serializers.ModelSerializer):
    colors = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    imageCover = serializers.ImageField(required=False)
    title = serializers.CharField(max_length=30,required=False)
    category = CategorySerializer(Category)
    brand = BrandSerializer(Brand)


    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description', 'quantity', 'sold', 'price','active','user', 'imageCover',
                  'images', 'colors',
                   'category', 'brand', 'createdAt', 'updatedAt', '_id']
        # fields = '__all__'

    def get_colors(self, obj):
        return [color.name for color in obj.colors.all()]

    def get_images(self, obj):
        return [image.img.url for image in obj.images.all()]
