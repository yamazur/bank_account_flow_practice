import pytest
from pages.add_customer_page import AddCustomerPage
from pages.open_account_page import OpenAccountPage

@pytest.mark.open_account_page
@pytest.mark.positive_test
class TestValidOpenAccount:
    def test_valid_open_account(self, browser):
        page = OpenAccountPage(browser)
        (page.open_page_and_checking_url()
            .customer_filling_of_drop_down_lists()
            .currency_filling_of_drop_down_lists()
            .process_click()
            .check_successful_open_account_alert()
            .go_to_customers_page()
            .checking_new_account_number(page.new_account_number)
         )
