import pytest
from pages.add_customer_page import AddCustomerPage

@pytest.mark.positive_test
class TestValidRegistration:
    def test_valid_registration(self, browser):
        page = AddCustomerPage(browser)
        (page.open_page_and_checking_url()
            .go_to_add_customer_page()
            .fill_fields_with_valid_data()
            .click_add_customer()
            .check_successful_alert()
            .checking_the_new_client_in_the_table())