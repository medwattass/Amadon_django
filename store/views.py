from django.shortcuts import render, redirect
from .models import Order, Product


def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def paycheck(request):
    quantity_from_form = int(request.POST["quantity"])
    id_product = int(request.POST["price"])
    price_from_form = Product.objects.get(id=id_product).price
    total_charge = quantity_from_form * price_from_form
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/paycheck/checkout')


def checkout(request):
    context = {
        "quantity": Order.objects.last().quantity_ordered,
        "price": Order.objects.last().total_price
    }
    return render(request, "store/checkout.html", context)