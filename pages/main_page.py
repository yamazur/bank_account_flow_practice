import allure
from pages.base_page import BasePage
from pages.locators import BankPracticeLocators


class MainPage(BasePage):

    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    @allure.step("Проверяем заголовок страницы")
    def find_title(self):
        expected_title = "XYZ Bank"
        actual_title = self.browser.find_element(*BankPracticeLocators.TITLE).text
        assert actual_title == expected_title, \
            f"Заголовок формы некорректен. Ожидалось: '{expected_title}', Получено: '{actual_title}'"
        return self

    @allure.step("Проверяем наличие формы")
    def find_form(self):
        return self.wait_for_element(BankPracticeLocators.FORM)
