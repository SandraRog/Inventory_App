from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

#CRUD-Create, Read, Update, Delete

# Home view
def home_view(request):
    return render(request, 'invAppT/home.html')

#create view
def product_create_view(request):
    form = ProductForm() #klasa stworzona w forms.py
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invAppT/product_form.html', {'form': form})
    #return render... - gdy jest to GET to wyswietla sie formularz

#read view
def product_list_view(request):
    products=Product.objects.all() #odnosi sie do modelu Product
    return render(request, 'invAppT/product_list.html', {'products': products})

#update view - konieczne tutaj id, bo update dotyczy danego produktu
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product) #musi byc instancja, bo pobieramy juz wczesniej zapisany produkt z bazy
        if form.is_valid():
            form.save()
            return redirect('product_list')
    #a jezeli metoda jest GET to:
    return render(request, 'invAppT/product_form.html', {'form': form})

#delete - podobne do update, bo musimy miec id zeby dokladnie ten produkt usunac
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invAppT/product_confirm_delete.html', {'product': product})
#obowiazkowy kontekst zeby wiedziec dokladnie ktory produkt