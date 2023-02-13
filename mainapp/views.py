from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Item
from django.conf import settings
import stripe


API_KEY = settings.STRIPE_SECRET_KEY


def index(request):
    all_items = Item.objects.all()

    return render(request, 'mainapp/index.html', {'all_items': all_items})


def item(request, pk):
    item = get_object_or_404(Item, id=pk)
    return render(request, 'mainapp/item.html', {'item': item})


def buy(request, pk):
    # check whether Item object exitsts 
    item = get_object_or_404(Item, id=pk)

    # passing an stripe secret key
    stripe.api_key = API_KEY

    # creating a stripe checkout session
    checkout_session = stripe.checkout.Session.create(
        line_items=[
        # item being bought, here we pass the product pice API ID and the number of products
            {
                'price': 'price_1MacxtDRiSKa1HSTKl624fdv',
                'quantity': 1,
            },
        ],
        mode='payment',
        # url to which the user is going to be redirected after success or cancellation
        success_url='http://localhost:8000',
        cancel_url='http://localhost:8000',
    )

    return redirect(checkout_session.url, code=303)
