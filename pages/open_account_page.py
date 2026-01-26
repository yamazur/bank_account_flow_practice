from pages.base_page import BasePage
import allure
from pages.locators import BankPracticeLocators

class OpenAccountPage(BasePage):

    # url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount"
    #
    # @allure.step("Открываем страницу и проверяем URL и элементы страницы")
    # def open_and_check(self):
    #     return self.open_page_and_checking_url()

    @allure.step("Проверка элементов формы")
    def should_be_elements_in_open_account_page(self):

        self.is_element_present(
            BankPracticeLocators.CUSTOMER_DROPDOWN,
            BankPracticeLocators.CURRENCY_DROPDOWN,
            BankPracticeLocators.PROCESS_BUTTON,
        )

    @allure.step("Успешный выбор значений из обоих выпадающих списков")
    def valid_filling_of_drop_down_lists(self):
        customer_dropdown = self.browser.find_element(*BankPracticeLocators.CUSTOMER_DROPDOWN)
        customer_dropdown.click()





