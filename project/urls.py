"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

def get_url_link(url):
    return 'api/' + url

@api_view(['GET'])
@permission_classes([AllowAny])
def root(request):
    return Response([
        {"postman collection":'https://www.postman.com/interstellar-station-543920/workspace/django-ecommerce-api/collection/14788230-5b06dde3-90ae-4cde-9e77-df739e34a40f'},

        get_url_link('admin/'),

        get_url_link('brands/'),
        get_url_link('brands/brand ID/'),

        get_url_link('categories/'),
        get_url_link('categories/category ID/'),

        get_url_link('coupons/'),
        get_url_link('coupons/coupon Name/'),

        get_url_link('products/'),
        get_url_link('products/product ID/'),

        get_url_link('reviews/'),
        get_url_link('reviews/review ID/'),

        get_url_link('reviews/product/product ID'),
        get_url_link('reviews/product/product ID/change/review ID/'),

        get_url_link('user/wishlist/'),
        get_url_link('user/wishlist/product ID/'),
        get_url_link('user/wishlist/clear/'),

        get_url_link('cart/'),
        get_url_link('cart/product ID'),
        get_url_link('cart/clear/'),

        get_url_link('orders/'),

        get_url_link('auth/token/'),
        get_url_link('auth/register/'),

        get_url_link('auth/token/refresh/'),
        get_url_link('auth/token/verify/'),

        get_url_link('auth/users/reset_password/'),
        get_url_link('auth/users/reset_password_confirm/'),

        get_url_link('user/'),
        get_url_link('auth/users/set_password/'),

        get_url_link('user/addresses/'),
        get_url_link('user/addresses/address ID/'),

        get_url_link('users/'),
        get_url_link('users/user ID/'),
    ])


urlpatterns = [
    path('',root),
    path('api/',root),
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/brands/', include('brands.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/coupons/', include('coupons.urls')),
    path('api/products/', include('products.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/user/', include('users.urls')),
    path('api/users/', include('users_admin.urls')),
    path('api/cart/', include('carts.urls')),
    path('api/orders/', include('orders.urls')),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]

urlpatterns += staticfiles_urlpatterns()

