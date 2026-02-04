import pytest

@pytest.mark.positive_test
class TestSearchForClients:
    def test_search_for_clients_by_full_name(self, customers_page):
        (customers_page
            .should_be_elements_in_customers_page()
            .search_customer("Hermoine")
            .is_customer_present("Hermoine")
         )

    def test_search_for_clients_by_part_name(self, customers_page):
        (customers_page
            .search_customer("Herm")
            .is_customer_present("Hermoine")
         )
