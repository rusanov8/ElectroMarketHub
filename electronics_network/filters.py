import django_filters

from .models import Network


class CountryFilter(django_filters.FilterSet):
    """
        Filter for the Network model based on the contact's country.
    """

    country = django_filters.CharFilter(field_name='contact__country', distinct=True)

    class Meta:
        model = Network
        fields = ['country']