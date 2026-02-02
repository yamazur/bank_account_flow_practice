import pytest
from pages.add_customer_page import AddCustomerPage
from pages.locators import BankPracticeLocators
from pages.open_account_page import OpenAccountPage

@pytest.mark.open_account_page
@pytest.mark.positive_test
class TestValidOpenAccount:
    def test_valid_open_account(self, browser):
        page = OpenAccountPage(browser)
        (page.open_page_and_checking_url()
            .should_be_elements_in_open_account_page()
            .customer_select()
            .currency_select()
            .click_element(BankPracticeLocators.PROCESS_BUTTON, description='"Process" button')
            .check_successful_open_account_alert()
            .go_to_customers_page()
            .checking_new_account_number()
         )
