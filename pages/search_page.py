from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, 'twotabsearchtextbox')
        self.search_button = (By.ID, 'nav-search-submit-button')
        self.no_result_message = (By.XPATH, "//span[normalize-space()='ld345tsxslfer']")

    def enter_search_term(self, term):
        self.driver.find_element(*self.search_box).clear()
        self.driver.find_element(*self.search_box).send_keys(term)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()

    def verify_no_results(self):
        return self.driver.find_element(*self.no_result_message).is_displayed()
