import pytest
from pages.add_customer_page import AddCustomerPage
from pages.locators import BankPracticeLocators


@pytest.mark.add_customer_page
@pytest.mark.negative_test
class TestAddDuplicateCustomer:
    def test_add_duplicate_customer(self, browser, customer_data):
        page = AddCustomerPage(browser)

        (page.open_page_and_checking_url()
            .fill_fields_with_existing_data()
            .click_element(BankPracticeLocators.ADD_CUSTOMER_BUTTON, description='"Add customer" button')
            .check_failed_alert()
            .go_to_customers_page()
            .checking_the_duplicate_client({'first_name': 'Hermoine', 'last_name': 'Granger', 'post_code': 'E859AB'}))
