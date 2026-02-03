import allure
from pages.locators import BankPracticeLocators


class NavigationMixin:
    @allure.step("Переходим на страницу списка клиентов")
    def go_to_customers_page(self):
        self.wait_for_element(BankPracticeLocators.GO_TO_CUSTOMERS_PAGE).click()
        return self

    @allure.step("Переходим на страницу создания клиента")
    def go_to_add_customer_page(self):
        self.wait_for_element(BankPracticeLocators.GO_TO_ADD_CUSTOMER_PAGE).click()
        return self
