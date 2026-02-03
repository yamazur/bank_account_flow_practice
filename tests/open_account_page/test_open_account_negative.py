import pytest
from pages.locators import BankPracticeLocators

@pytest.mark.open_account_page
@pytest.mark.negative_test
class TestInvalidOpenAccount:
    def test_invalid_open_account(self, open_account_page):
        (open_account_page
            .currency_select()
            .click_element(BankPracticeLocators.PROCESS_BUTTON, description='"Process" button')
            .checking_no_alert()
         )
