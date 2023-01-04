import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class HomePage(BasePage):
    HOME_PAGE_TITLE = 'Home Page - Magento eCommerce'
    GLOBAL_SEARCH = (By.ID, "search")
    HOME_LOGO = (By.CSS_SELECTOR, ".logo")

    def verify_home_pageTitle(self):
        assert self.HOME_PAGE_TITLE in self.get_pageTitle(), "Login page is not loaded."

    def verify_globalSearch_isPresent(self):
        self.is_element_present(self.GLOBAL_SEARCH)

    def navigate_to_homePage(self):
        self.is_element_present(self.HOME_LOGO)
        self.do_click(self.HOME_LOGO)

