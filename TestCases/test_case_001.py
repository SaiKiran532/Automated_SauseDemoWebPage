import time
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Testcase001:
    pageurl = ReadConfig.get_Application_url()
    username = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    scree_shot_path = "C:\\Users\\saikiran.challa\\PycharmProjects\\pythonProject5\\Screenshots\\test_homepage_title.png"

    def test_homepage_title(self, setup):
        self.logger.info("********** Testcase001 ********** ")
        self.logger.info("********** Verifying Homepage Title **********")

        self.driver = setup
        self.driver.get(self.pageurl)
        time.sleep(2)
        actual_title1 = self.driver.title
        if actual_title1 == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("********** Homepage title test passed **********")
        else:
            self.driver.save_screenshot(self.scree_shot_path)
            self.driver.close()
            self.logger.error("********** Homepage title test failed **********")
            assert False

    def test_login(self, setup):
        self.logger.info("********** Login testcase started **********")
        self.logger.info("********** Verifying CartPage Url **********")
        self.driver = setup
        self.driver.get(self.pageurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        curr_url = self.driver.current_url
        if curr_url == "https://www.saucedemo.com/v1/inventory.html":
            assert True
            self.logger.info("********** CartPage Url test passed **********")
        else:
            self.driver.save_screenshot(self.scree_shot_path)
            self.logger.error("********** CartPage Url test failed **********")
            assert False
        self.lp.clickThreeLineButton()
        self.lp.clickLogout()
        self.driver.close()
