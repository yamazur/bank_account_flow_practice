import pytest
from pages.locators import BankPracticeLocators


@pytest.mark.add_customer_page
@pytest.mark.positive_test
class TestValidRegistration:
    def test_valid_registration(self, add_customer_page, customer_data):
        (add_customer_page
            .should_be_elements_in_add_customer_page()
            .fill_fields_with_valid_data(customer_data)
            .click_element(BankPracticeLocators.ADD_CUSTOMER_BUTTON, description='"Add customer" button')
            .check_successful_alert()
            .go_to_customers_page()
         )
        assert add_customer_page.is_customer_present(customer_data['post_code'])
