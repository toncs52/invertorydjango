from django.shortcuts import redirect, render

from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'frontend/index.html', {'products': products})

def product_detail(request , id):
    products = Product.objects.get(id=id)
    return render(request, 'frontend/product_detail.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        product = Product(
            product_name = request.POST['product_name'],
            product_detail = request.POST['product_detail'],
            product_barcode = request.POST['product_barcode'],
            product_qty = request.POST['product_qty'],
            product_price = request.POST['product_price'],
            product_image = request.POST['product_image'],
            product_status = request.POST['product_status'],
        )
        product.save()
        return redirect('/')
    else:
        return render(request , 'frontend/product_create.html')

def product_delete(request , id):
    products = Product.objects.get(id=id)
    products.delete()
    return redirect('/')