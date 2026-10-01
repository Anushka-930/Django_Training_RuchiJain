from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Product


def saveuser(request):

    products = [
        (101, "Laptop", 50000, 10),
        (102, "Mobile", 25000, 15),
        (103, "Tablet", 18000, 10),
        (104, "Keyboard", 1500, 5),
        (105, "Mouse", 800, 10),
        (106, "Monitor", 12000, 20),
        (107, "Headphones", 2000, 15),
        (108, "Printer", 15000, 10),
        (109, "Smartwatch", 5000, 20),
        (110, "Speaker", 3000, 5),
    ]

    for pid, name, price, offer in products:
        product = Product(
            pid=pid,
            pname=name,
            pprice=price,
            poffer=offer
        )
        product.save()

    return HttpResponse("10 Products saved successfully")


def productlist(request):  # Read record
    products = Product.objects.all()
    res = render(request, 'productlist.html', {'products': products})
    return res

def updateproduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.pid = request.POST['pid']
        product.pname = request.POST['pname']
        product.pprice = request.POST['pprice']
        product.poffer = request.POST['poffer']
        product.save()
        return HttpResponseRedirect(reverse('productlist'))

    return render(request, 'updateproduct.html', {'product': product})

def deleteproduct(request, product_id):
    if request.method != 'POST':
        return HttpResponse(status=405)

    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('productlist'))