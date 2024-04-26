import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.AddToCartPage import AddToCartPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestCase002:
    pageurl = ReadConfig.get_Application_url()
    username = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()
    first_name = "SomeFirstName"
    last_name = "SomeLastName"
    postal_code = "504251"

    def test_add_items_to_cart(self, setup):
        self.logger.info("********** Login testcase started **********")
        self.driver = setup
        self.driver.get(self.pageurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.cartpage = AddToCartPage(self.driver)
        self.cartpage.addItemToCart()
        self.logger.info("********** Items added to Cart **********")

        self.cartpage.clickCartIcon()
        self.cartpage.clickCheckOut()
        self.logger.info("********** Checkout Successful **********")
        self.cartpage.enterDetails(self.first_name, self.last_name, self.postal_code)
        self.logger.info("********** Details added Successfully **********")
        self.cartpage.clickSubmit()
        self.cartpage.clickFinish()
        self.logger.info("********** Order finished **********")

        if self.cartpage.verifySuccessMsg() == 'THANK YOU FOR YOUR ORDER':
            print("Test completed successfully")
        else:
            print("Test failed")
        self.logger.info("********** Verification done **********")
        self.driver.close()




