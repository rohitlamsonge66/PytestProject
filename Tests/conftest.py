import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None


@pytest.fixture(scope="class")
def init_driver(request):
    print('---------------------------setup----------------------------------')
    options = webdriver.ChromeOptions()
    # options.headless = True
    we_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    we_driver.maximize_window()
    we_driver.implicitly_wait(10)  # seconds
    request.cls.driver = we_driver
    yield
    print('-------------------------------Tear Down------------------------------------')
    we_driver.quit()
