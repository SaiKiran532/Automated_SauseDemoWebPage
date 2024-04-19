import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
class TestcaseDDT:
    pageurl = ReadConfig.get_Application_url()
    data_path = "C:\\Users\\saikiran.challa\\PycharmProjects\\pythonProject5\\TestData\\LoginData.xlsx"
    logger = LogGen.log_gen()

    scree_shot_path = "C:\\Users\\saikiran.challa\\PycharmProjects\\pythonProject5\\Screenshots\\test_login_ddt.png"
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*********** TestcaseDDT **********")
        self.logger.info("********** Login DDT testcase started **********")
        self.logger.info("********** Verifying Homepage Title **********")
        self.driver = setup
        self.driver.get(self.pageurl)
        self.lp = LoginPage(self.driver)


        self.rows = XLUtils.getRowCount(self.data_path, 'Sheet1')
        print("Number of rows in a Excel:", self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.data_path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.data_path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.data_path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)

            act_url = self.driver.current_url
            exp_url = "https://www.saucedemo.com/v1/inventory.html"

            if act_url == exp_url:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clickThreeLineButton()
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.driver.save_screenshot(self.scree_shot_path)
                    self.logger.info("**** failed ****")
                    self.lp.clickThreeLineButton()
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_url != exp_url:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TestcaseDDT ************* ");




