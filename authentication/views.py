from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer


# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            password = request.data.get('password')
            if password:
                # if not user.check_password(password):
                #     return Response({"password":'the password is not valid'})
                user.set_password(password)
                user.is_active = True
                user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
