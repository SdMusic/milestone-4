from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's currently nothing in your cart")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JDTZuKJLyYKB5lvAXvTxsVXQylZPgWKTbu6TXkZSw3TXAp532Pet4Y8dZHauKJ2ybgIESItezw7RaB9MK7OXoJX00XD2mUWTw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
