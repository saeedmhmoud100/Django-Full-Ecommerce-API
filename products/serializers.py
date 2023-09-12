from rest_framework import serializers

from products.models import Image, Color, Product


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    colors = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    imageCover = serializers.ImageField(required=False)
    title = serializers.CharField(max_length=30,required=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description', 'quantity', 'sold', 'price','active', 'imageCover',
                  'images', 'colors',
                  'user', 'category', 'brand', 'createdAt', 'updatedAt', '_id']
        # fields = '__all__'

    def get_colors(self, obj):
        return [color.name for color in obj.colors.all()]

    def get_images(self, obj):
        return [image.img.url for image in obj.images.all()]
