import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)

time.sleep(10)

def login():
    form_login = driver.find_element(By.ID, "user-name")
    form_password = driver.find_element(By.ID, "password")
    form_submit = driver.find_element(By.ID, "login-button")
    form_login.send_keys("standard_user")
    form_password.send_keys("secret_sauce")
    form_submit.click()

def add_to_card():
    item = driver.find_element(By.CSS_SELECTOR, ".inventory_item_description .pricebar .btn")
    item_title = driver.find_element(By.CSS_SELECTOR, ".inventory_item_description .inventory_item_name")
    item_title = item_title.text
    item.click()
    cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart.click()
    cart_element_title = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div")
    cart_element_title = cart_element_title.text
    assert item_title in cart_element_title, "В корзине должен быть ранее выбранный товар"

def checkout():
    checkout_button = driver.find_element(By.CSS_SELECTOR, ".checkout_button")
    checkout_button.click()
    checkout_info_firstname = driver.find_element(By.CSS_SELECTOR, ".checkout_info #first-name")
    checkout_info_lastname = driver.find_element(By.CSS_SELECTOR, ".checkout_info #last-name")
    checkout_info_zip = driver.find_element(By.CSS_SELECTOR, ".checkout_info #postal-code")
    checkout_button_continue = driver.find_element(By.CSS_SELECTOR, ".checkout_buttons input[type='submit']")
    checkout_info_firstname.send_keys("test")
    checkout_info_lastname.send_keys("test")
    checkout_info_zip.send_keys("1234")
    checkout_button_continue.click()
    checkout_button_finish = driver.find_element(By.CSS_SELECTOR, ".cart_footer #finish")
    checkout_button_finish.click()
    checkout_complete = driver.find_element(By.CSS_SELECTOR, ".header_secondary_container .title")
    assert "Complete" in checkout_complete.text, "Во время покупки произошла ошибка"
    

def test_login():
    login()