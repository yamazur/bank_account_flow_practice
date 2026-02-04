from helpers.customer_factory import CustomerFactory
import pytest


@pytest.mark.positive_test
class TestDeleteCustomer:
    def test_delete_customer(self, browser, customers_page, customer_data):
        CustomerFactory.create_customer(browser, customer_data)
        customers_page.go_to_customers_page().delete_customer(customer_data['post_code'])
