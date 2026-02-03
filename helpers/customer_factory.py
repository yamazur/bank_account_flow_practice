import allure
from pages.add_customer_page import AddCustomerPage


class CustomerFactory:
    @staticmethod
    @allure.step('Создаем нового клиента')
    def create_customer(browser, customer_data):
        page = AddCustomerPage(browser)
        (page.open_page_and_checking_url()
            .fill_fields_with_valid_data(customer_data)
            .click_add_customer()
            .check_successful_alert()
         )
