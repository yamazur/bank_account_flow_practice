from selenium.webdriver.common.by import By

class BankPracticeLocators:

    #основное
    TITLE = (By.CSS_SELECTOR, "strong.mainHeading")
    FORM = (By.CSS_SELECTOR, "div.border.box.padT20.ng-scope")

    # add_customer
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='First Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    POST_CODE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Post Code']")
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "button[type='submit'].btn.btn-default")

    #open_account
    CUSTOMER_DROPDOWN = (By.ID, "userSelect")
    CURRENCY_DROPDOWN = (By.ID, "currency")
    PROCESS_BUTTON = (By.XPATH, "//button[text()='Process']")

    #customers
    TABLE_BODY = (By.CSS_SELECTOR, "table.table tbody")
    SEARCH_CUSTOMER_INPUT = (By.CSS_SELECTOR, "input[placeholder='Search Customer']")
    FIRST_NAME_SORT = (By.LINK_TEXT, "First Name")
    POST_CODE_SORT = (By.LINK_TEXT, "Post Code")
    DELETE_BUTTON = (By.XPATH, ".//button[text()='Delete']")

    #navigation
    GO_TO_ADD_CUSTOMER_PAGE = (By.XPATH, "//button[contains(text(), 'Add Customer')]")
    GO_TO_CUSTOMERS_PAGE = (By.XPATH, "//button[contains(text(), 'Customers')]")
