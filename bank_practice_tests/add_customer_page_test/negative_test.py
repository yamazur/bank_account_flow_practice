import pytest
from pages.add_customer_page import AddCustomerPage


@pytest.mark.add_customer_page
@pytest.mark.negative_test
class TestExistingUser:
    def test_existing_user(self, browser):
        page = AddCustomerPage(browser)
        (page.open_page_and_checking_url()
            .should_be_elements_in_add_customer_page()
            .fill_fields_with_existing_data()
            .click_add_customer()
            .check_failed_alert()
            .go_to_customers_page()
            .checking_the_duplicate_client()
         )

