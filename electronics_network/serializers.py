from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Product, Network, Contact


class ContactSerializer(serializers.ModelSerializer):
    """
           Serializer for the Contact model.
    """

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
       Serializer for the Product model.
    """

    class Meta:
        model = Product
        fields = "__all__"


class NetworkSerializer(serializers.ModelSerializer):
    """
       Serializer for the Network model.

       Meta:
           - model: Network
           - fields: "__all__"
           - read_only_fields: ('debt',)

       Methods:
           - get_supplier: Get serialized supplier data.
           - validate: Validate data based on the level.

       """

    contact = ContactSerializer()
    products = ProductSerializer(many=True, required=False)
    supplier = serializers.SerializerMethodField()

    class Meta:
        model = Network
        fields = "__all__"
        read_only_fields = ('debt',)

    @staticmethod
    def get_supplier(obj):
        if obj.supplier:
            return NetworkSerializer(obj.supplier).data
        return None

    def validate(self, data):

        level = data.get('level')
        supplier = data.get('supplier')
        debt = data.get('debt')

        if level == 0:
            if supplier is not None or (debt is not None and debt > 0):
                raise ValidationError(
                    _("A factory (level 0) cannot have a supplier or debt to the supplier.")
                )

        return data


