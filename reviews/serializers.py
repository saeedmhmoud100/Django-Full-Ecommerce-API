from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Reviews
from users.serializers import  UserSerializer2


class ReviewsSerializer(serializers.ModelSerializer):
    user = UserSerializer2(instance=get_user_model(),read_only=True)
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Reviews
        fields = ['id','review','rating','product','user','createdAt','updatedAt','_id']
