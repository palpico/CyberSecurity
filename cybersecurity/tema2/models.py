from django.db.models import Model, CharField, PositiveIntegerField, ForeignKey,\
    DecimalField, DateTimeField, PROTECT
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, RegexValidator, MaxValueValidator
from decimal import Decimal

# validadores
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', _('Only alphanumeric characters are allowed.'))
alphanumeric_spaces = RegexValidator(r'^[0-9a-zA-Z\s]*$', _('Only alphanumeric characters are allowed.'))


class User(Model):
    name = CharField(verbose_name=_("Nombre"), max_length=125, null=False, blank=False, validators=[alphanumeric])
    lastname = CharField(verbose_name=_("Apellido"), max_length=125, null=False, blank=False, validators=[alphanumeric])
    social_security = CharField(verbose_name=_("Seguro Social #"), max_length=9, null=False, blank=False,
                                validators=[alphanumeric])
    # validador de edad minima edad legal en varios paises, validador maximo solo mostrar el uso de varios validadores
    age = PositiveIntegerField(verbose_name=_("Edad"), null=False, blank=False,
                               validators=[MaxValueValidator(200), MinValueValidator(18)])
    address = CharField(verbose_name=_("Direccion"), max_length=125, null=False, blank=False,
                        validators=[alphanumeric_spaces])


class Product(Model):
    name = CharField(verbose_name=_("Nombre"), max_length=125, null=False, blank=False, validators=[alphanumeric])
    description = CharField(verbose_name=_("Descripcion"), max_length=125, null=False, blank=False, validators=[alphanumeric])
    provider = CharField(verbose_name=_("Proveedor"), max_length=125, null=False, blank=False, validators=[alphanumeric])
    price = DecimalField(verbose_name=_("Precio"), max_digits=15, decimal_places=2, null=False,
                         blank=False, validators=[MinValueValidator(Decimal('0.00'))], default=0.00)
    quantity = PositiveIntegerField(verbose_name=_("Cantidad"), null=False, blank=False, default=0)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Invoice(Model):
    sub_total = DecimalField(verbose_name=_("Sub total"), max_digits=15, decimal_places=2, null=False,
                             blank=False, validators=[MinValueValidator(Decimal('0.00'))], default=0.00)
    tax = DecimalField(verbose_name=_("Imouesto"), max_digits=15, decimal_places=2, null=False,
                       blank=False, validators=[MinValueValidator(Decimal('0.00'))], default=0.00)
    total = DecimalField(verbose_name=_("Total"), max_digits=15, decimal_places=2, null=False,
                         blank=False, validators=[MinValueValidator(Decimal('0.00'))], default=0.00)
    billing_name = CharField(verbose_name=_("Facturacion - nombre"), max_length=125, null=False, blank=False,
                             validators=[alphanumeric_spaces])
    billing_identification = CharField(verbose_name=_("Facturacion - identification"), max_length=125, null=False,
                                       blank=False, validators=[alphanumeric])
    billing_address = CharField(verbose_name=_("Facturacion - address"), max_length=125, null=False, blank=False,
                                validators=[alphanumeric_spaces])
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class InvoiceProduct(Model):
    fk_invoice_id = ForeignKey(Invoice, on_delete=PROTECT)
    fk_product_id = ForeignKey(Product, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Purchases(Model):
    fk_user_id = ForeignKey(User, on_delete=PROTECT)
    fk_invoice_id = ForeignKey(Invoice, on_delete=PROTECT)
    payment_method = CharField(verbose_name=_("Payment method"), max_length=125, null=False, blank=False,
                               validators=[alphanumeric])
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Login(Model):
    fk_user_id = ForeignKey(User, on_delete=PROTECT)
    email = CharField(verbose_name=_("Email"), max_length=125, null=False, blank=False,
                      validators=[alphanumeric_spaces])
    password = CharField(verbose_name=_("Password"), max_length=125, null=False, blank=False,
                         validators=[alphanumeric_spaces])
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
