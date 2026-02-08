from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import DEFAULT_TIMEOUT
import allure


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(DEFAULT_TIMEOUT)

    @allure.step('Открываем страницу и проверяем URL')
    def open_page_and_checking_url(self):
        self.browser.get(self.url)
        assert self.browser.current_url == self.url, \
            f"Expected URL {self.url}, but got {self.browser.current_url}"
        return self

    @allure.step("Ожидание появления элемента")
    def wait_for_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Применяем ожидание элемета к каждому локатору")
    def is_element_present(self, *locators):
        for locator in locators:
            element = self.wait_for_element(locator)
            assert element is not None, f"Element {locator} is missing"

    @allure.step("Ожидание кликабельности элемента и клик по элементу")
    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        click_element = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        click_element.click()
        return self

    @allure.step("Проверяем отсутствие элемента")
    def is_not_element_present(self, locators, timeout=DEFAULT_TIMEOUT):  # абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locators))
        except TimeoutException:
            return True

    @allure.step("Ожидание появления элемента")
    def wait_for_alert(self, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.browser, timeout).until(
            EC.alert_is_present()
        )

    @allure.step("Поиск клиента в табоице")
    def is_value_present_in_table(self, locators, value: str) -> bool:
        table = self.browser.find_element(*locators)
        return value in table.text

    @allure.step("Хэлпер для поиска и заполнения инпутов")
    def _fill_input(self, locator, value: str):
        element = self.browser.find_element(*locator)
        element.clear()
        element.send_keys(value)

    @allure.step("Клик по элементу")
    def click_element(self, locators, description=None):
        step_name = f'Клик по {description}'
        with allure.step(step_name):
            self.browser.find_element(*locators).click()
        return self
