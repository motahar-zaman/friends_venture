"""
URL configuration for friends_venture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework import routers
from django.urls import path, include
from friends_venture.views import health_check, home, delete_partner, partner_details
from friends_venture.views import PartnerViewSet, TransactionViewSet

router = routers.DefaultRouter()

router.register(r'partner', PartnerViewSet, 'partners')
router.register(r'transaction', TransactionViewSet, 'transactions')

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('check/', health_check, name='health_check'),
    path('delete-partner/<id>', delete_partner, name='delete_partner'),
    path('partner-details/<id>', partner_details, name='partner_details'),
]
