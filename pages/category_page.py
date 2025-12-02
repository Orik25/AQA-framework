from .base_page import BasePage


class CategoryPage(BasePage):
    CURRENT_CATEGORY = ".portal__heading"

    def get_current_category(self):
        return self.find(self.CURRENT_CATEGORY).text