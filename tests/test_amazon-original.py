from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_driver_path = r"C:\Users\prati\OneDrive\Documents\chromedriver.exe"

# Use Service to specify the path to chromedriver
service = Service(chrome_driver_path)

# Initialize WebDriver with the service argument
driver = webdriver.Chrome(service=service)

original_window = driver.current_window_handle

driver.maximize_window()
driver.implicitly_wait(10)
def test_search_non_existing_product():
    driver.get('https://www.amazon.in/')
    #Enter in Search Bar
    driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("ld345tsxslfer")
    #Click on Search
    driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
    #verify that No Result found is displayed
    no_result_found = driver.find_element(By.XPATH, "//span[normalize-space()='ld345tsxslfer']")
    assert no_result_found.is_displayed()

def test_search_laptop():
    driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").clear()
    driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Laptop")
    # Click on Search
    driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
    #verify that Laptop is displayed
    laptop_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert laptop_text == '"Laptop"'

def test_4thproduct_in_cart():
    product_name = driver.find_element(By.XPATH, "//span[@class='rush-component s-latency-cf-section']/div/div[6]/div/div/span/div/div/div/div[2]/div/div/div/h2/a/span").text
    print(product_name)
    price = driver.find_element(By.XPATH, "(//span[@class='a-price'])[4]").text
    print("Price-", price)
    driver.find_element(By.XPATH, "//span[@class='rush-component s-latency-cf-section']/div/div[6]/div/div/span/div/div/div/div[2]/div/div/div/h2/a").click()
    # Get all window handles
    all_windows = driver.window_handles

    # Switch to the new tab
    for window_handle in all_windows:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    #Click on Add to Cart
    driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']").click()
    #Added to Cart saved to message variable
    message = driver.find_element(By.XPATH, "(//h4[@class='a-alert-heading'][normalize-space()='Added to Cart'])[2]")
    #waiting for the element to be visible
    cart = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@id='attach-accessory-cart-subtotal']"))
    )
    cart_price = driver.find_element(By.XPATH, "//span[@id='attach-accessory-cart-subtotal']").text
    assert message.is_displayed()


def test_update_quantity():
    #Clicking on View Cart Button
    driver.find_element(By.XPATH, "//input[@aria-labelledby='attach-sidesheet-view-cart-button-announce']").click()
    #saving price of first added item to price_of_quantity variable
    price_of_quantity = driver.find_element(By.XPATH, "//span[@id='sc-subtotal-amount-activecart']//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']").text
    #removing the , from the price
    price_cleaned = float(price_of_quantity.strip().replace(',', ''))
    #clicking on quantity dropdown and selecting quantity
    driver.find_element(By.ID, "a-autoid-0-announce").click()
    #saving text for number of quantity and clicking the same
    quantity = driver.find_element(By.XPATH, "(//a[normalize-space()='2'])[1]").text
    driver.find_element(By.XPATH, "(//a[normalize-space()='2'])[1]").click()
    time.sleep(2)
    #getting the new price after updating quantity
    price_after_updated_quantity = driver.find_element(By.XPATH, "//span[@id='sc-subtotal-amount-activecart']//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']").text
    price_cleaned_1 = float(price_after_updated_quantity.strip().replace(',', ''))
    print("Price in Cart-",price_after_updated_quantity)
    assert (int(price_cleaned) * int(quantity)) == int(price_cleaned_1)

def test_remove_from_cart():
    #driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[5]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[3]/div[4]/div[1]/div[3]/div[1]/span[2]/span[1]/input[1]").click()
    driver.find_element(By.XPATH, "(//div[@class='sc-item-content-group'])[1]/div[1]/span[2]/span/input").click()
    #driver.find_element(By.XPATH, "(//a[normalize-space()='0 (Delete)'])[1]").click()
    time.sleep(2)
    empty_message = driver.find_element(By.XPATH, "//h2[normalize-space()='Your Amazon Cart is empty.']").text
    assert 'Your Amazon Cart is empty.' in empty_message