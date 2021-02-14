# Generated by Django 3.0.12 on 2021-02-13 22:10

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Sub total')),
                ('tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Imouesto')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Total')),
                ('billing_name', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\s]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Facturacion - nombre')),
                ('billing_identification', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Facturacion - identification')),
                ('billing_address', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\s]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Facturacion - address')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Nombre')),
                ('description', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Descripcion')),
                ('provider', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Proveedor')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Precio')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Cantidad')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Apellido')),
                ('social_security', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Seguro Social #')),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(18)], verbose_name='Edad')),
                ('address', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\s]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Payment method')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fk_invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tema2.Invoice')),
                ('fk_user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tema2.User')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\s]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Email')),
                ('password', models.CharField(max_length=125, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\s]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Password')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fk_user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tema2.User')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fk_invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tema2.Invoice')),
                ('fk_product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tema2.Product')),
            ],
        ),
    ]