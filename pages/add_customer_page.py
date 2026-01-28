import allure
from faker import Faker
from pages.base_page import BasePage
from pages.locators import BankPracticeLocators

class AddCustomerPage(BasePage):

    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    def __init__(self, browser):
        super().__init__(browser, self.URL)
        self.created_customer_data = {}

    @allure.step('Переходим в раздел "Add Customer"')
    def go_to_add_customer_page(self):
        self.wait_for_element(BankPracticeLocators.ADD_CUSTOMER_BUTTON).click()
        return self

    @allure.step('Заполняем поля валидно')
    def fill_valid_required(self):

        self.is_element_present(
            BankPracticeLocators.FIRST_NAME_INPUT,
            BankPracticeLocators.LAST_NAME_INPUT,
            BankPracticeLocators.POST_CODE_INPUT,
            BankPracticeLocators.ADD_CUSTOMER_BUTTON
        )

        fake = Faker()

        #генерируем и сохраняем данные
        self.created_customer_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'post_code': fake.postcode()
        }

        #имя
        first_name_input = self.browser.find_element(*BankPracticeLocators.FIRST_NAME_INPUT)
        first_name_input.clear()
        first_name_input.send_keys(
            self.created_customer_data['first_name']
        )

        #фамилия
        last_name_input = self.browser.find_element(*BankPracticeLocators.LAST_NAME_INPUT)
        last_name_input.clear()
        last_name_input.send_keys(
            self.created_customer_data['last_name']
        )

        #посткод
        post_code_input = self.browser.find_element(*BankPracticeLocators.POST_CODE_INPUT)
        post_code_input.clear()
        post_code_input.send_keys(
            self.created_customer_data['post_code']
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
        alert_expected_text = "Customer added successfully with customer id:"
        assert alert_expected_text in alert_actual_text, \
            f"В алерте написано: {alert_actual_text} ожидалось: {alert_expected_text}"
        alert.accept()
        return self

    @allure.step('Проверяем, что клиент появился в таблице Customers')
    def checking_the_new_client_in_the_table(self):
        post_code = self.created_customer_data['post_code']
        table_body = self.browser.find_element(*BankPracticeLocators.TABLE_BODY)
        table_text = table_body.text
        return post_code in table_text




