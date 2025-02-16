from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        #labels nieobowiazkowe, ale pola formularzu beda bardziej czytelne, widniec beda nazwy etykiet
        widgets={
            'product_id': forms.NumberInput(attrs={'placeholder':'eg. 1', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'eg. shirt', 'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder':'eg. S1234', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder':'eg. 19.99', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder':'eg. 10', 'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder':'eg. ABC', 'class': 'form-control'}),

        }
        #widgets-definiuja typ pol formularza, np data, liczba, tekst, atrybuty moga zawierac elementy CSS