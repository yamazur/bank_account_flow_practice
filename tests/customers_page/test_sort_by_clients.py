from pages.locators import BankPracticeLocators
import pytest


@pytest.mark.positive_test
class TestSortByClients:
    def test_sort_by_clients_by_name(self, customers_page):
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