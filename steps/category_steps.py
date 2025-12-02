from framework.dsl import given, when, then

@then("Category should be '(.*)'")
def check_category(ctx, expected_category):
    category_page = ctx.pages["category"]
    actual = category_page.get_current_category()
    assert actual == expected_category, f"Expected category '{expected_category}', but got '{actual}'"

