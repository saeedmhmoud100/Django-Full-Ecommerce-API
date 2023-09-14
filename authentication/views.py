from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.serializers import UserSerializer


# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        password = request.data.get('password')
        if password:
            if len(password) < 8:
                return Response({"password":'the password is not valid'})
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.is_active = True
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
