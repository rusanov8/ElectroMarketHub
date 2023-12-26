from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CountryFilter

from .models import Network, Product, Contact
from .serializers import NetworkSerializer, ProductSerializer, ContactSerializer
from .permissions import IsActive


class NetworkViewSet(viewsets.ModelViewSet):
    """
        ViewSet for the Network model.

        Attributes:
        - queryset: Queryset for the Network model.
        - serializer_class: Serializer class for the Network model.
        - permission_classes: List of permission classes, includes IsActive.
        - filter_backends: List of filter backends, includes DjangoFilterBackend.
        - filterset_class: FilterSet class for the Network model.
    """

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountryFilter


class ProductViewSet(viewsets.ModelViewSet):
    """
        ViewSet for the Product model.

        Attributes:
        - queryset: Queryset for the Product model.
        - serializer_class: Serializer class for the Product model.
        - filter_backends: List of filter backends, includes SearchFilter.
        - search_fields: List of searchable fields for the Product model.
        - permission_classes: List of permission classes, includes IsActive.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'model']
    permission_classes = [IsActive]


class ContactViewSet(viewsets.ModelViewSet):
    """
        ViewSet for the Contact model.

        Attributes:
        - queryset: Queryset for the Contact model.
        - serializer_class: Serializer class for the Contact model.
        - permission_classes: List of permission classes, includes IsActive.
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsActive]

