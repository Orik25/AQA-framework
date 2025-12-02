from framework.dsl import given, when, then
from pages.cart_page import CartPage


@when("I open cart")
def open_cart(ctx):
    results = ctx.pages["results"]
    results.open_cart()
    ctx.pages["cart"] = CartPage(ctx.driver)

@when("I delete item from cart")
def delete_item_from_cart(ctx):
    cart = ctx.pages["cart"]
    cart.delete_item()
    ctx.pages["cart"] = CartPage(ctx.driver)


@then("Cart should contains '(.*)' items")
def open_cart(ctx, expected_items_count):
    cart = ctx.pages["cart"]
    actual_items_count = cart.get_items_count()
    expected_items_count = int(expected_items_count)

    assert actual_items_count == expected_items_count, (
        f"Expected {expected_items_count} items, but found {actual_items_count}"
    )

