from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Item, Order
from django.conf import settings
from django.contrib import messages
import stripe


API_KEY = settings.STRIPE_SECRET_KEY


def index(request):
    all_items = Item.objects.all()
    orders = Order.objects.all()

    return render(request, 'mainapp/index.html', {'all_items': all_items, 'orders': orders})


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
        # item being bought, here we pass the product details
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': item.price * 100,
                    'product_data': {
                        'name': item.name
                    },
                },
                # 'price': 'price_1MacxtDRiSKa1HSTKl624fdv',
                'quantity': 1,
            },
        ],
        mode='payment',
        # url to which the user is going to be redirected after success or cancellation
        success_url='http://localhost:8000',
        cancel_url='http://localhost:8000',
    )
    
    messages.success(request, 'Order successfully paid')
    return redirect(checkout_session.url, code=303)



def buy_order(request, pk):
    order = Order.objects.get(id=pk)
    items = order.items.all()
    price = order.overall_price()

    stripe.api_key = API_KEY

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': price * 100,
                    'product_data': {
                        'name': 'Order #' + str(order.id)
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://localhost:8000',
        cancel_url='http://localhost:8000',
    )

    messages.success(request, 'Order successfully paid')
    return redirect(checkout_session.url, code=303)
