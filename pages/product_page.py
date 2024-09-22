from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_name_locator = (By.XPATH, "//span[@class='rush-component s-latency-cf-section']/div/div[6]/div/div/span/div/div/div/div[2]/div/div/div/h2/a/span")
        self.add_to_cart_button = (By.ID, 'add-to-cart-button')

    def get_product_name(self):
        return self.driver.find_element(*self.product_name_locator).text

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
