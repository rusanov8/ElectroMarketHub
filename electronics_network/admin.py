from django.contrib import admin
from electronics_network.models import Product, Network, Contact
from django.utils.html import format_html
from rest_framework.reverse import reverse


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """
       Custom admin configuration for the Network model.
    """

    list_display = ('id', 'name', 'level', 'supplier_link', 'debt', 'created_at')
    fields = ('name', 'level', 'supplier', 'debt', 'contact', 'products')
    list_filter = ('contact__city',)

    actions = ['clear_debt']

    def supplier_link(self, obj):
        """
            Generates a link to the supplier in the admin interface.
        """

        if obj.supplier:
            link = reverse("admin:electronics_network_network_change", args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier.name)
        return "-"
    supplier_link.short_description = 'Supplier'

    def clear_debt(self, request, queryset):
        """
            Action to clear the debt of selected networks.
        """
        queryset.update(debt=0)

    clear_debt.short_description = "Clear debt of selected"


admin.site.register(Contact)
admin.site.register(Product)




