import allure
from pages.base_page import BasePage
from pages.locators import BankPracticeLocators


class CustomersPage(BasePage):

    @allure.step("Переходим в раздел Customers")
    def go_to_customers_page(self):
        self.wait_for_element(BankPracticeLocators.GO_TO_CUSTOMERS_PAGE).click()
        return self