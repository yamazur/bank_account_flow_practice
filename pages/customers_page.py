import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import BankPracticeLocators
from pages.navigation_mixin import NavigationMixin


class CustomersPage(BasePage, NavigationMixin):

    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"

    def __init__(self, browser):
        super().__init__(browser, self.URL)
        # self.created_customer_data = {}

    @allure.step("Проверка элементов формы")
    def should_be_elements_in_customers_page(self):
        self.is_element_present(
            BankPracticeLocators.SEARCH_CUSTOMER_INPUT,
            BankPracticeLocators.TABLE_BODY,
        )
        return self

    @allure.step('В поле Search Customer вводим значение: "{value}"')
    def search_customer(self, value: str):
        search_input = self.wait_for_element(BankPracticeLocators.SEARCH_CUSTOMER_INPUT)
        search_input.clear()
        search_input.send_keys(value)
        return self

    @allure.step('Проверяем, что значение "{value}" есть в таблице Customers')
    def is_customer_present(self, value: str):
        table_body = self.wait_for_element(BankPracticeLocators.TABLE_BODY)
        return value in table_body.text

    @allure.step('Сортировка клиентов')
    def sort_customers(self, header_locator, column_index: int, descending: bool = False):

        step_name = f"Сортировка колонки {column_index} по {'убыванию' if descending else 'возрастанию'}"

        with allure.step(step_name):
            #клик по заголовку
            self.wait_for_element(header_locator).click()

            #берем все значения из колонки
            table = self.wait_for_element(BankPracticeLocators.TABLE_BODY)
            values = [row.text for row in table.find_elements(By.XPATH, f"./tr/td[{column_index}]")]

            #проверяем сортировку
            assert values == sorted(values, reverse=descending), (
                f"Колонка {column_index} не отсортирована "
                f"{'по убыванию' if descending else 'по возрастанию'}: {values}"
            )

        return self

    @allure.step('Удаление клиента')
    def delete_customer(self, post_code):
        #находим клиента, которого хотим удалить
        row = self.browser.find_element(By.XPATH, f"//tr[td[text()='{post_code}']]")

        #находим кнопку delete в этой строке и кликаем
        delete_button = row.find_element(*BankPracticeLocators.DELETE_BUTTON)
        delete_button.click()

        #проверяем, что клиента в таблице нет
        table_text = self.browser.find_element(*BankPracticeLocators.TABLE_BODY).text
        assert post_code not in table_text, \
            f"Пользователь с post_code {post_code} не удален"

        return self
