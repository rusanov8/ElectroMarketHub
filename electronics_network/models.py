from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class Contact(models.Model):
    """
        Model representing contact information.

        Attributes:
            - email (EmailField): Email address of the contact.
            - country (CharField): Country of the contact.
            - city (CharField): City of the contact.
            - street (CharField): Street of the contact.
            - house_number (CharField): House number of the contact.

        Methods:
            - __str__: Returns a string representation of the contact.

        Meta:
            - verbose_name: Singular name for the model.
            - verbose_name_plural: Plural name for the model.
            - db_table: Database table name for the model.

    """

    email = models.EmailField(verbose_name=_('Contact Email'))
    country = models.CharField(max_length=100, verbose_name=_('Country'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    street = models.CharField(max_length=100, verbose_name=_('Street'))
    house_number = models.CharField(max_length=20, verbose_name=_('House Number'))

    def __str__(self):
        return f'{self.email} - {self.country}, {self.city}, {self.street}, {self.house_number}'

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        db_table = 'contacts'


class Network(models.Model):
    """
      Model representing a network with contact information, products, supplier, and debt.

      Attributes:
          - LEVEL_CHOICES (list): Choices for the 'level' field.
          - name (CharField): Name of the network.
          - level (IntegerField): Level of the network (Factory, Retail Network, Individual Entrepreneur).
          - contact (OneToOneField): One-to-one relationship with the Contact model.
          - products (ManyToManyField): Many-to-many relationship with the Product model.
          - supplier (ForeignKey): Foreign key relationship with itself, representing the supplier network.
          - debt (DecimalField): Debt to the supplier.
          - created_at (DateTimeField): Date and time of creation.

      Methods:
          - __str__: Returns a string representation of the network.
          - clean: Custom validation to ensure that a factory (level 0) cannot have a supplier or debt.

      Meta:
          - verbose_name: Singular name for the model.
          - verbose_name_plural: Plural name for the model.
          - db_table: Database table name for the model.

      """

    LEVEL_CHOICES = [
        (0, _('Factory')),
        (1, _('Retail Network')),
        (2, _('Individual Entrepreneur')),
    ]

    name = models.CharField(max_length=255, verbose_name=_('Name'), db_index=True)
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name=_('Level'))

    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name=_('Contact Information'))
    products = models.ManyToManyField('Product', verbose_name=_('Products'), related_name='networks')

    supplier = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_networks', verbose_name=_('Supplier'), db_index=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_('Debt to Supplier'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Time'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Network')
        verbose_name_plural = _('Networks')
        db_table = 'networks'

    def clean(self):
        """
            Custom validation to ensure that a factory (level 0) can not have a supplier or debt.

            Raises:
                ValidationError: If the validation conditions are not met.

        """

        level = self.level

        if level == 0:
            supplier = self.supplier
            debt = self.debt

            if supplier is not None or (debt is not None and debt > 0):
                raise ValidationError(
                    _("A factory (level 0) cannot have a supplier or debt to the supplier.")
                )


class Product(models.Model):
    """
       Model representing a product with a name, model, and release date.
    """

    name = models.CharField(max_length=255, verbose_name=_('Name'), db_index=True)
    model = models.CharField(max_length=100, verbose_name=_('Model'))
    release_date = models.DateTimeField(verbose_name=_('Release Date'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        db_table = 'products'
