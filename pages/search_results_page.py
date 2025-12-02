from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re, time

from .base_page import BasePage


class SearchResultsPage(BasePage):
    SORT_BUTTON = "#sort"
    PRODUCT_TITLES = ".tile-title.black-link.text-base"
    PRODUCT_PRICES = ".price.text-2xl.color-red"

    LANGUAGE_TOGGLE = "[data-testid='lang_btn']"
    BUY_BUTTON = ".buy-button"
    CART_BUTTON = "[data-testid='header-cart-btn']"

    @staticmethod
    def lang_button(lang_code):
        return f"//button[normalize-space()='{lang_code}']"

    def sort_by_price_asc(self):
        time.sleep(2)
        select_element = self.find(by=By.ID, value="sort")
        select = Select(select_element)
        select.select_by_value("cheap")

    def sort_by_price_desc(self):
        time.sleep(2)
        select_element = self.find(by=By.ID, value="sort")
        select = Select(select_element)
        select.select_by_value("expensive")

    def get_titles(self):
        return [el.text for el in self.find_all(self.PRODUCT_TITLES)]

    def get_prices(self):
        prices = [el.text for el in self.find_all(self.PRODUCT_PRICES)]
        return [int(re.sub(r"\D", "", p)) for p in prices]

    def change_language(self, lang_code):
        time.sleep(2)
        self.click(self.LANGUAGE_TOGGLE)
        time.sleep(2)
        self.click(by=By.XPATH, value=self.lang_button(lang_code.upper()))

    def get_language(self):
        return self.find(value=self.LANGUAGE_TOGGLE).text

    def buy_first_item(self):
        time.sleep(2)
        self.click(self.BUY_BUTTON)

    def open_cart(self):
        time.sleep(2)
        self.click(self.CART_BUTTON)
