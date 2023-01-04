import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_HomePage(BaseTest):
    def test_HomePage(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        home_page.navigate_to_homePage()
        home_page.verify_home_pageTitle()
        home_page.verify_globalSearch_isPresent()
