import allure
from pages.base_page import BasePage
from pages.locators import BankPracticeLocators
from pages.navigation_mixin import NavigationMixin


class AddCustomerPage(BasePage, NavigationMixin):

    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust"

    def __init__(self, browser):
        super().__init__(browser, self.URL)


    @allure.step('Проверка элементов формы')
    def should_be_elements_in_add_customer_page(self):

        self.is_element_present(
            BankPracticeLocators.FIRST_NAME_INPUT,
            BankPracticeLocators.LAST_NAME_INPUT,
            BankPracticeLocators.POST_CODE_INPUT,
            BankPracticeLocators.ADD_CUSTOMER_BUTTON
        )
        return self

    @allure.step('Заполняем поля валидно')
    def fill_fields_with_valid_data(self, customer_data: dict):
        self.browser.find_element(*BankPracticeLocators.FIRST_NAME_INPUT).clear()
        self.browser.find_element(*BankPracticeLocators.FIRST_NAME_INPUT).send_keys(
            customer_data['first_name']
        )

        self.browser.find_element(*BankPracticeLocators.LAST_NAME_INPUT).clear()
        self.browser.find_element(*BankPracticeLocators.LAST_NAME_INPUT).send_keys(
            customer_data['last_name']
        )

        self.browser.find_element(*BankPracticeLocators.POST_CODE_INPUT).clear()
        self.browser.find_element(*BankPracticeLocators.POST_CODE_INPUT).send_keys(
            customer_data['post_code']
        )

        return self

    @allure.step('Нажимаем кнопку "Add customer"')
    def click_add_customer(self):
        self.browser.find_element(*BankPracticeLocators.ADD_CUSTOMER_BUTTON).click()
        return self

    @allure.step('Проверяем, что высвечивается alert с подтверждением создания клиента и закрываем его')
    def check_successful_alert(self):
        self.wait_for_alert()
        alert = self.browser.switch_to.alert

        alert_actual_text = alert.text
        alert_expected_text = "Customer added successfully with customer id :"

        assert alert_expected_text in alert_actual_text, \
            f"В алерте написано: {alert_actual_text} ожидалось: {alert_expected_text}"

        alert.accept()
        return self

    @allure.step('Проверяем, что клиент появился в таблице Customers')
    def is_customer_present(self, value: str) -> bool:
        return self.is_value_present_in_table(BankPracticeLocators.TABLE_BODY,value)

    @allure.step('Заполняем поля с уже существующими данными (например, Hermoine Granger E859AB)')
    def fill_fields_with_existing_data(self):

        # данные
        customer = {'first_name': 'Hermoine', 'last_name': 'Granger', 'post_code': 'E859AB'}

        # имя
        self.browser.find_element(*BankPracticeLocators.FIRST_NAME_INPUT).clear()
        self.browser.find_element(*BankPracticeLocators.FIRST_NAME_INPUT).send_keys(customer['first_name'])

        # фамилия
        self.browser.find_element(*BankPracticeLocators.LAST_NAME_INPUT).clear()
        self.browser.find_element(*BankPracticeLocators.LAST_NAME_INPUT).send_keys(customer['last_name'])

        # посткод
        self.browser.find_element(*BankPracticeLocators.POST_CODE_INPUT).clear()
        self.browser.find_element(*BankPracticeLocators.POST_CODE_INPUT).send_keys(customer['post_code'])

        return self

    @allure.step('Проверяем alert о дубликате клиента')
    def check_failed_alert(self):
        self.wait_for_alert()
        alert = self.browser.switch_to.alert

        alert_actual_text = alert.text
        alert_expected_text = "Please check the details. Customer may be duplicate."

        assert alert_expected_text in alert_actual_text, \
            f"В алерте написано: {alert_actual_text} ожидалось: {alert_expected_text}"

        alert.accept()
        return self

    @allure.step('Проверяем, что клиент не появился в таблице Customers, дубликата нет')
    def checking_the_duplicate_client(self, value: str):
        table_text = self.browser.find_element(*BankPracticeLocators.TABLE_BODY).text
        count = table_text.split().count(value)

        assert count <= 1, \
            f"Значение '{value}' найдено {count} раз, ожидалось не более 1"

        return self
