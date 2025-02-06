import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(amount, product):
    """ create_stripe_price """
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product=product,
    )


def create_stripe_product(name):
    """create_stripe_product"""
    product = stripe.Product.create(name=name)
    return product.get("id")


def create_stripe_session(price):
    """ create_stripe_session """
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
