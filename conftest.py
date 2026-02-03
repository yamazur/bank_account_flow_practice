import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from config import DEFAULT_TIMEOUT
from pages.add_customer_page import AddCustomerPage
from pages.customers_page import CustomersPage
from pages.open_account_page import OpenAccountPage


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
def add_customer_page(browser):
    page = AddCustomerPage(browser)
    page.open_page_and_checking_url()
    return page

@pytest.fixture
def open_account_page(browser):
    page = OpenAccountPage(browser)
    page.open_page_and_checking_url()
    return page

@pytest.fixture
def customers_page(browser):
    page = CustomersPage(browser)
    page.open_page_and_checking_url()
    return page
