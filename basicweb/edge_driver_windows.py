import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class EdgeWebDriver():
    driver = None
    def __init__(self,url):
        self.url = url

    def launch_web_app(self):
        edgeService = EdgeService(executable_path="D:\\softwares\\browserDrivers\\edgedriver_win64\\msedgedriver.exe")
        self.driver = webdriver.Edge(service=edgeService)
        self.driver.get(self.url)
        self.driver.maximize_window()
        return self

    def navigate_to_userSignIn(self):
        elementById = self.driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
        if elementById is not None:
            elementById.click()
        return self

    def user_input_username(self):
        username_textfield_id = "ap_email_login"
        username_textfield = self.driver.find_element(By.ID, username_textfield_id)
        if username_textfield is not None:
            username_textfield.send_keys("<username>")
        continue_button_id="continue"
        continue_button = self.driver.find_element(By.ID, continue_button_id)
        if continue_button is not None:
            continue_button.click()
        return self

    def user_input_password_and_signin(self):
        password_textfield_id = "ap_password"
        password_textfield = self.driver.find_element(By.ID, password_textfield_id)
        if password_textfield is not None:
            password_textfield.send_keys("<password>")
        sign_in_button_id = 'signInSubmit'
        sign_in_button = self.driver.find_element(By.ID, sign_in_button_id)
        if sign_in_button is not None:
            sign_in_button.click()
        print(self.driver.title)
        time.sleep(3)
        return self

    def search_product_in_home_search_box(self, productSearch):
        search_box_id = "twotabsearchtextbox"
        search_box = self.driver.find_element(By.ID, search_box_id)
        if search_box is not None:
            search_box.send_keys(productSearch)
        start_search_button_id = "nav-search-submit-button"
        start_search_button = self.driver.find_element(By.ID, start_search_button_id)
        if start_search_button is not None:
            start_search_button.click()
        return self

    def add_to_cart_from_search_results(self):
        add_to_cart_xpath \
= "//span[contains(text(), \"OnePlus Nord 4 5G (Oasis Green, 8GB RAM, 256GB Storage)\")]//ancestor::div[2]//child::div[3]//button"
        add_to_cart = self.driver.find_element(By.XPATH, add_to_cart_xpath)
        if add_to_cart is not None:
            add_to_cart.click()
            time.sleep(3)
        return self

    def check_cart(self):
        cart_count_element_xpath = "//div[@id=\"nav-cart-count-container\"]/span[1]"
        cart_count_element = self.driver.find_element(By.XPATH, cart_count_element_xpath)
        if cart_count_element is not None:
            if cart_count_element.text == "1":
                print("one product added to cart")
        return self

edgeBrowserTest = EdgeWebDriver(url='https://www.amazon.in')
(edgeBrowserTest
 .launch_web_app()
 .navigate_to_userSignIn()
 .user_input_username()
 .user_input_password_and_signin()
 .search_product_in_home_search_box("OnePlus Nord 4 5G (Oasis Green, 8GB RAM, 256GB Storage)")
 #.add_to_cart_from_pdp()
 .add_to_cart_from_search_results()
 .check_cart())
#driver=edgeBrowserTest.launch_web_app("https://www.amazon.in")
#edgeBrowserTest.navigate_to_userSignIn(driver)