from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [path('admin/', admin.site.urls)] + router.urls
