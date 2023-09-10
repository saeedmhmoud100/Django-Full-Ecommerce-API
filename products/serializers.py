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
    images = serializers.ImageField()
    class Meta:
        model = Product
        fields = ['id','title','slug','description','quantity','sold','price','imageCover',
                  'images','colors',
                  'user','category','brand', 'createdAt','updatedAt','_id']
        # fields = '__all__'

    def get_colors(self,obj):
        return [color.name for color in obj.colors.all()]
