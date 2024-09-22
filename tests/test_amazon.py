import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#import sys
#import os
#print(sys.path)
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

chrome_driver_path = r"C:\Users\prati\OneDrive\Documents\chromedriver.exe"
service = Service(chrome_driver_path)

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_search_non_existing_product(driver):
    search_page = SearchPage(driver)
    driver.get('https://www.amazon.in/')
    search_page.enter_search_term("ld345tsxslfer")
    search_page.click_search()
    assert search_page.verify_no_results()

def test_search_laptop(driver):
    search_page = SearchPage(driver)
    search_page.enter_search_term("Laptop")
    search_page.click_search()
    assert '"Laptop"' in driver.page_source

def test_4thproduct_in_cart(driver):
    product_page = ProductPage(driver)
    search_page = SearchPage(driver)
    cart_page = CartPage(driver)

    search_page.enter_search_term("Laptop")
    search_page.click_search()
    product_name, product_price = product_page.get_fourth_product_details()
    print("Product:", product_name, "Price:", product_price)

    product_page.select_fourth_product()
    product_page.add_to_cart()
    assert "Added to Cart" in driver.page_source

def test_update_quantity(driver):
    cart_page = CartPage(driver)
    cart_page.update_quantity_to_2()
    # Add additional assertions for quantity and price comparison

def test_remove_from_cart(driver):
    cart_page = CartPage(driver)
    cart_page.remove_item()
    assert "Your Amazon Cart is empty" in cart_page.verify_cart_is_empty()
