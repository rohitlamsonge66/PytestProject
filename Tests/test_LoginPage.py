import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.verify_login_pageTitle()
        print("***************************Login method*************************************")
        self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)

