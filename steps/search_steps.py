import time

from framework.dsl import given, when, then
from pages.cart_page import CartPage
from pages.search_results_page import SearchResultsPage

@when(r"I search for '(.*)'")
def search(ctx, query):
    home = ctx.pages["home"]
    home.search(query)
    ctx.pages["results"] = SearchResultsPage(ctx.driver)

@when(r"I add first item to cart")
def search(ctx):
    results = ctx.pages["results"]
    results.buy_first_item()

@then("search results should contain '(.*)'")
def check(ctx, query):
    titles = ctx.pages["results"].get_titles()
    assert len(titles) > 0, "No search results found!"

    matching = [t for t in titles if query.lower() in t.lower()]
    assert len(matching) > 0, f"No search results contain '{query}'"
