import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class EdgeWebDriver():
    driver = None
    cart_quantity = 0
    userName = ""
    password = ""

    def __init__(self,url):
        self.url = url
        load_dotenv(override=True)
        self.userName = os.getenv('username')
        self.password = os.getenv('password')

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
            username_textfield.send_keys(self.userName)
        continue_button_id="continue"
        continue_button = self.driver.find_element(By.ID, continue_button_id)
        if continue_button is not None:
            continue_button.click()
        return self

    def user_input_password_and_signin(self):
        password_textfield_id = "ap_password"
        password_textfield = self.driver.find_element(By.ID, password_textfield_id)
        if password_textfield is not None:
            password_textfield.send_keys(self.password)
        sign_in_button_id = 'signInSubmit'
        sign_in_button = self.driver.find_element(By.ID, sign_in_button_id)
        if sign_in_button is not None:
            sign_in_button.click()
        print(self.driver.title)
        #time.sleep(3)
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
            = "//span[contains(text(), \"OnePlus Nord 4 5G (Obsidian Midnight, 8GB RAM, 256GB Storage)\")]//ancestor::div[2]//child::div[3]//button"
        add_to_cart = self.driver.find_element(By.XPATH, add_to_cart_xpath)
        if add_to_cart is not None:
            time.sleep(5)
            add_to_cart.click()
            time.sleep(3)
        return self

    def add_to_cart_from_pdp(self):
        link_to_pdp_xpath = "//span[contains(text(), \"OnePlus Nord 4 5G (Oasis Green, 8GB RAM, 256GB Storage)\")]//ancestor::a"
        link_to_pdp = self.driver.find_element(By.XPATH, link_to_pdp_xpath)
        product_title_in_pdp_id = "productTitle"
        add_to_cart_in_pdp_id = "add-to-cart-button"
        buy_now_button_id = "buy-now-button"
        if link_to_pdp is not None:
            link_to_pdp.click()

            time.sleep(5)
            currentWindowHandle = self.driver.current_window_handle
            handles = self.driver.window_handles
            for handle in handles:
                if handle not in currentWindowHandle:
                    self.driver.switch_to.window(handle)
                    product_title_element = self.driver.find_element(By.ID, product_title_in_pdp_id)
                    if product_title_element is not None:
                        if str(product_title_element.text).__contains__(
                                "OnePlus Nord 4 5G (Oasis Green, 8GB RAM, 256GB Storage)"):
                            print("In product details page")
                            break
        #buy_now_button = self.driver.find_element(By.ID, buy_now_button_id)
        #if buy_now_button is not None:
            add_to_cart_in_pdp = self.driver.find_element(By.ID, add_to_cart_in_pdp_id)
            if add_to_cart_in_pdp is not None:
                time.sleep(3)
                wait = WebDriverWait(self.driver, timeout=10, poll_frequency=2, ignored_exceptions=[ElementNotInteractableException])
                wait.until(EC.element_to_be_clickable(add_to_cart_in_pdp))
                add_to_cart_in_pdp.click()
        return self

    def check_cart(self):
        cart_count_element_xpath = "//div[@id=\"nav-cart-count-container\"]/span[1]"
        cart_count_element = self.driver.find_element(By.XPATH, cart_count_element_xpath)
        if cart_count_element is not None:
            self.cart_quantity = int(cart_count_element.text)
            print(f"cart quantity - {self.cart_quantity}")
        return self