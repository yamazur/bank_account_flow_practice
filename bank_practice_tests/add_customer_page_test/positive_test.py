import pytest
from pages.add_customer_page import AddCustomerPage
from pages.open_account_page import OpenAccountPage


@pytest.mark.add_customer_page
@pytest.mark.positive_test
class TestValidRegistration:
    def test_valid_registration(self, browser):
        page = AddCustomerPage(browser)
        (page.open_page_and_checking_url()
            .should_be_elements_in_add_customer_page()
            .fill_fields_with_valid_data()
            .click_add_customer()
            .check_successful_alert()
            .go_to_customers_page()
            .checking_the_new_client_in_the_table())


