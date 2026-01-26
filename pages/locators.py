from selenium.webdriver.common.by import By

class BankPracticeLocators:

    #основное
    TITLE = (By.CSS_SELECTOR, "strong.mainHeading")

    #open_account
    CUSTOMER_DROPDOWN = (By.ID, "userSelect")

    CURRENCY_DROPDOWN = (By.ID, "currency")
    PROCESS_BUTTON = (By.XPATH, "//button[text()='Process']")



