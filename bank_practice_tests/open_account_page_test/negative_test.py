import pytest
from pages.add_customer_page import AddCustomerPage
from pages.open_account_page import OpenAccountPage


@pytest.mark.open_account_page
@pytest.mark.negative_test
class TestValidOpenAccount:
    def test_valid_open_account(self, browser):
        page = OpenAccountPage(browser)
        (page.open_page_and_checking_url()
            .currency_filling_of_drop_down_lists()
            .process_click()
            .checking_no_alert()
         )
