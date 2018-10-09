"""insider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path, include
from insider import views

urlpatterns = [
    path('', views.index),

    # auth
    path('rest-auth/password/confirm/<uidb64>/<token>/', views.password_reset_confirm,
         name='password_reset_confirm'),
    path('rest-auth/registration/account-confirm-email/<str:key>/', views.account_confirm_email,
         name='account_confirm_email'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('', include('houses.urls')),
    path('', include('flats.urls'))
]
