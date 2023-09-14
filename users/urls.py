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
from django.urls import path
from users.views import WishList, wishlistChange, clearWishlist, LoggedUser, UserAddressesListView, \
    UserAddressesDetailsView

urlpatterns = [

    path('wishlist', WishList.as_view()),
    path('wishlist/clear', clearWishlist),
    path('wishlist/<int:pk>', wishlistChange),


    path('', LoggedUser.as_view()),
    path('addresses', UserAddressesListView.as_view()),
    path('addresses/<int:pk>', UserAddressesDetailsView.as_view()),

]


