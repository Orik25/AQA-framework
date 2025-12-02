import time

from .base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = "ul.cart-list li.cart-list__item"
    MORE_BUTTON = "#cartProductActions0"
    DELETE_ITEM_BUTTON = ".button.button--medium.button--with-icon.button--link"

    def get_items_count(self):
        time.sleep(4)
        try:
            return len(self.find_all(self.CART_ITEMS))
        except Exception:
            return 0

    def delete_item(self):
        self.click(self.MORE_BUTTON)
        self.click(self.DELETE_ITEM_BUTTON)
