import pytest
from pages.main_page import MainPage


@pytest.mark.smoke_test
class TestDisplayingTheBankForm:
    def test_displaying_the_bank_form(self, browser):
        page = MainPage(browser)
        page.open_page_and_checking_url().find_title().find_form()