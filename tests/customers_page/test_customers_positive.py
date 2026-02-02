from pages.locators import BankPracticeLocators


class TestSearchForClients:
    def test_search_for_clients_by_full_name(self, customers_page):
        """Поиск клиента по полному имени"""
        (customers_page
         .should_be_elements_in_customers_page()
         .search_customer("Hermoine")
         .is_customer_present("Hermoine")
         )

    def test_search_for_clients_by_part_name(self, customers_page):
        """Поиск клиента по части имени"""
        (customers_page
         .search_customer("Herm")
         .is_customer_present("Hermoine")
         )

class TestSortByClients:
    def test_sort_by_clients_by_name(self, customers_page):
        """Сортировка клиентов по First Name"""
        (customers_page
            .sort_customers(
            header_locator=BankPracticeLocators.FIRST_NAME_SORT,
            column_index=1,
            descending=True  # проверка первого клика - обратный алфавиту
        )
            .sort_customers(
            header_locator=BankPracticeLocators.FIRST_NAME_SORT,
            column_index=1,
            descending=False  # проверка второго клика - по алфавиту
         ))

    def test_sort_by_clients_by_postcode(self, customers_page):
        """Сортировка клиентов по Postcode"""
        (customers_page
            .sort_customers(
            header_locator=BankPracticeLocators.POST_CODE_SORT,
            column_index=3,
            descending=True  # проверка первого клика - на уменьшение
        )
        .sort_customers(
            header_locator=BankPracticeLocators.POST_CODE_SORT,
            column_index=3,
            descending=False  # проверка второго клика - на увеличение
        ))

class TestDeleteCustomer:
    def test_delete_customer(self, client):
        pass
