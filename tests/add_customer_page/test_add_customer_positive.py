import pytest
from pages.add_customer_page import AddCustomerPage
from pages.locators import BankPracticeLocators
from pages.open_account_page import OpenAccountPage


@pytest.mark.add_customer_page
@pytest.mark.positive_test
class TestValidRegistration:
    def test_valid_registration(self, browser, customer_data):
        page = AddCustomerPage(browser)

        (page.open_page_and_checking_url()
            .should_be_elements_in_add_customer_page()
            .fill_fields_with_valid_data(customer_data)
            .click_element(BankPracticeLocators.ADD_CUSTOMER_BUTTON, description='"Add customer" button')
            .check_successful_alert()
            .go_to_customers_page()
         )
        assert page.is_customer_present(customer_data['post_code'])
