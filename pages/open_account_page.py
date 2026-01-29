from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from config import DEFAULT_TIMEOUT
from pages.base_page import BasePage
import allure
from pages.locators import BankPracticeLocators

class OpenAccountPage(BasePage):

    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount"

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    @allure.step("Проверка элементов формы")
    def should_be_elements_in_open_account_page(self):

        self.is_element_present(
            BankPracticeLocators.CUSTOMER_DROPDOWN,
            BankPracticeLocators.CURRENCY_DROPDOWN,
            BankPracticeLocators.PROCESS_BUTTON,
        )

    @allure.step("Успешный выбор из  выпадающего списка Customer")
    def customer_filling_of_drop_down_lists(self):
        select_customer = Select(self.browser.find_element(*BankPracticeLocators.CUSTOMER_DROPDOWN))
        select_customer.select_by_value('1')
        return self

    @allure.step("Успешный выбор из  выпадающего списка Currency")
    def currency_filling_of_drop_down_lists(self):
        select_currency = Select(self.browser.find_element(*BankPracticeLocators.CURRENCY_DROPDOWN))
        select_currency.select_by_value('Dollar')
        return self

    @allure.step('Клик по кнопке "Process"')
    def process_click(self):
        self.browser.find_element(*BankPracticeLocators.PROCESS_BUTTON).click()
        return self

    @allure.step('Проверяем, что вспывает alert с текстом "Account created successfully with account Number :" и номером счета')
    def check_successful_open_account_alert(self):

        #проверяем, что это нужный алерт
        self.wait_for_alert()
        alert = self.browser.switch_to.alert
        alert_actual_text = alert.text
        alert_expected_text = "Account created successfully with account Number :"
        assert alert_expected_text in alert_actual_text, \
            f"В алерте написано: {alert_actual_text} ожидалось: {alert_expected_text}"

        #сохраняем номер созданного счета из алерта
        new_account_number = alert_actual_text.split(":")[-1].strip()
        self.new_account_number = new_account_number

        #закрываем алерт
        alert.accept()

        return self

    @allure.step('Проверяем, что счет появился в таблице Customers')
    def checking_new_account_number(self, new_account_number):

        #находим строку гермионы
        hermoine_row = self.browser.find_element(By.XPATH, "//tr[td[1]='Hermoine']")

        #берем всю строку
        row_text = hermoine_row.text

        assert str(new_account_number) in row_text.split(), \
            f"Счет {new_account_number} не найден у Гермионы"

        return self

    @allure.step('Проверяем, что alert об успешном создании счета не всплывает')
    def checking_no_alert(self):
        try:
            WebDriverWait(self.browser, DEFAULT_TIMEOUT).until(EC.alert_is_present())

            # если алерт появился (берем его текст для отчета)
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()

            raise AssertionError(
                f"Неожиданно появился алерт!\n"
                f"Текст алерта: {alert_text}\n"
            )

        except TimeoutException:
            return self


    @allure.step("Переходим на страницу списка клиентов")
    def go_to_customers_page(self):
        self.wait_for_element(BankPracticeLocators.GO_TO_CUSTOMERS_PAGE).click()
        return self

