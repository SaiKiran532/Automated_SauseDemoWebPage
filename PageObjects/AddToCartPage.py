
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Locators.Locators import Locators


class AddToCartPage(Locators):

    def __init__(self, driver):    # this constructor will get driver from testcase, and initialise it with current local driver.
        self.driver = driver

    def addItemToCart(self):
        self.driver.find_element(By.XPATH, self.cart_item1_loc_xpath).click()
        self.driver.find_element(By.XPATH, self.cart_item2_loc_xpath).click()

    def clickCartIcon(self):
        self.driver.find_element(By.XPATH, self.cart_icon_loc_xpath).click()

    def clickCheckOut(self):
        self.driver.find_element(By.XPATH, self.checkout_loc_xpath).click()

    def enterDetails(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, self.first_name_loc_id).clear()
        self.driver.find_element(By.ID, self.first_name_loc_id).send_keys(first_name)

        self.driver.find_element(By.ID, self.last_name_loc_id).clear()
        self.driver.find_element(By.ID, self.last_name_loc_id).send_keys(last_name)

        self.driver.find_element(By.ID, self.postal_code_loc_id).clear()
        self.driver.find_element(By.ID, self.postal_code_loc_id).send_keys(postal_code)

    def clickSubmit(self):
        self.driver.find_element(By.XPATH, self.submit_button_loc_xpath).click()


    def clickFinish(self):
        self.driver.find_element(By.XPATH, self.finish_button_loc_xpath).click()

    def verifySuccessMsg(self):
        return self.driver.find_element(By.XPATH, self.order_success_loc_xpath).text




