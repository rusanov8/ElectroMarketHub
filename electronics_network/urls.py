from rest_framework.routers import DefaultRouter
from .views import NetworkViewSet, ProductViewSet, ContactViewSet
from .apps import ElectronicsNetworkConfig

app_name = ElectronicsNetworkConfig.name

router = DefaultRouter()
router.register(r'networks', NetworkViewSet, basename='network')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'contacts', ContactViewSet, basename='contacts')

urlpatterns = router.urls

