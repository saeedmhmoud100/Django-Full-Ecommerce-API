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
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/brands/', include('brands.urls')),
    path('api/coupons/', include('coupons.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/products/', include('products.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/user/', include('users.urls')),
    path('api/users/', include('users_admin.urls')),
    path('api/cart/', include('carts.urls')),
    path('api/orders/', include('orders.urls')),
]

urlpatterns += staticfiles_urlpatterns()
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

