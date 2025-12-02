from selenium.webdriver.common.by import By

from .base_page import BasePage

class HomePage(BasePage):

    URL = "https://rozetka.com.ua/"

    SEARCH_FIELD = "input[name='search']"
    SEARCH_BUTTON = "button[type='submit']"

    CATEGORY_BUTTON = "[aria-label='Каталог']"
    @staticmethod
    def category_option(category_opt: str) -> str:
        return f"//a[@data-testid='fat_menu_category_link' and normalize-space(.) = '{category_opt}']"

    def open_home(self):
        self.open(self.URL)

    def search(self, query):
        self.type(self.SEARCH_FIELD, query)
        self.click(self.SEARCH_BUTTON)

    def open_category(self, category):
        self.click(self.CATEGORY_BUTTON)
        self.click(By.XPATH, self.category_option(category))
