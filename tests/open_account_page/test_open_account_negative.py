import pytest
from pages.locators import BankPracticeLocators
from pages.open_account_page import OpenAccountPage

@pytest.mark.open_account_page
@pytest.mark.negative_test
class TestInvalidOpenAccount:
    def test_invalid_open_account(self, browser):
        page = OpenAccountPage(browser)
        (page.open_page_and_checking_url()
            .currency_select()
            .click_element(BankPracticeLocators.PROCESS_BUTTON, description='"Process" button')
            .checking_no_alert()
         )
