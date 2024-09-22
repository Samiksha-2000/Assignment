from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_price = (By.XPATH, "//span[@id='attach-accessory-cart-subtotal']")
        self.update_quantity_dropdown = (By.ID, "a-autoid-0-announce")
        self.quantity_2 = (By.XPATH, "(//a[normalize-space()='2'])[1]")
        self.remove_button = (By.XPATH, "(//div[@class='sc-item-content-group'])[1]/div[1]/span[2]/span/input")
        self.empty_cart_message = (By.XPATH, "//h2[normalize-space()='Your Amazon Cart is empty.']")

    def verify_cart_price(self):
        return self.driver.find_element(*self.cart_price).text

    def update_quantity_to_2(self):
        self.driver.find_element(*self.update_quantity_dropdown).click()
        self.driver.find_element(*self.quantity_2).click()

    def remove_item(self):
        self.driver.find_element(*self.remove_button).click()

    def verify_cart_is_empty(self):
        return self.driver.find_element(*self.empty_cart_message).text
