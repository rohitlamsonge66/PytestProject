from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.HomePage import HomePage

""""Page Action for Login Page"""


class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    SIGNIN = (By.ID, "send2")
    LOGIN_PAGE_TITLE = 'Customer Login Magento Commerce'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # def get_login_page_Title(self):
    #     return self.get_pageTitle()

    def verify_login_pageTitle(self):
        assert self.LOGIN_PAGE_TITLE in self.get_pageTitle(), "Login page is not loaded."

    def login(self, email, password):
        self.do_EnterText(self.EMAIL, email)
        self.do_EnterText(self.PASSWORD, password)
        self.do_click(self.SIGNIN)
        return HomePage(self.driver)

