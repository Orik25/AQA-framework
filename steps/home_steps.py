from framework.dsl import given, when, then
from pages.category_page import CategoryPage


@when("I choose category '(.*)'")
def open_cart(ctx, category):
    home = ctx.pages["home"]
    home.open_category(category)
    ctx.pages["category"] = CategoryPage(ctx.driver)