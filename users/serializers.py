from django.contrib.auth import get_user_model
from rest_framework import serializers

from brands.models import Brand


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


