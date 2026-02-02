import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from config import DEFAULT_TIMEOUT
from pages.customers_page import CustomersPage


@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, DEFAULT_TIMEOUT)

@pytest.fixture
def customer_data(browser):
    fake = Faker()
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'post_code': fake.postcode()
    }

@pytest.fixture
def customers_page(browser):
    page = CustomersPage(browser)
    page.open_page_and_checking_url()
    return page