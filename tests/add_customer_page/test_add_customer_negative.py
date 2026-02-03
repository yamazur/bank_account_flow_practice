import pytest
from pages.locators import BankPracticeLocators


@pytest.mark.add_customer_page
@pytest.mark.negative_test
class TestAddDuplicateCustomer:
    def test_add_duplicate_customer(self, add_customer_page, customer_data):
        (add_customer_page
            .fill_fields_with_existing_data()
            .click_element(BankPracticeLocators.ADD_CUSTOMER_BUTTON, description='"Add customer" button')
            .check_failed_alert()
            .go_to_customers_page()
            .checking_the_duplicate_client({'first_name': 'Hermoine', 'last_name': 'Granger', 'post_code': 'E859AB'}))
