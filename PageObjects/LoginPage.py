from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    username_loc_id = "user-name"
    password_loc_id = "password"
    button_loc_id = "login-button"
    butoon_three_line_fea_loc_xpath = "//button[contains(text(),'Open Menu')]"
    logout_loc_linktext = "Logout"

    def __init__(self, driver):    # this constructor will get driver from testcase, and initialise it with current local driver.
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.username_loc_id).clear()
        self.driver.find_element(By.ID, self.username_loc_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_loc_id).clear()
        self.driver.find_element(By.ID, self.password_loc_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_loc_id).click()

    def clickThreeLineButton(self):
        self.driver.find_element(By.XPATH, self.butoon_three_line_fea_loc_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_loc_linktext).click()



