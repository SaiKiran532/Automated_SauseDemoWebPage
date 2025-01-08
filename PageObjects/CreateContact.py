import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Locators.Locators import Locators

class CreateContact(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def create_contact(self, salutation, first_name, last_name,existing_account):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element(By.XPATH, self.account_tab)).click().perform()
            time.sleep(3)
            action.move_to_element(self.driver.find_element(By.XPATH, self.existing_account.format(existing_account))).click().perform()
            time.sleep(5)
            action.move_to_element(self.driver.find_element(By.XPATH, self.new_contact)).click().perform()
            time.sleep(5)

            # Fill out the contact form
            action.move_to_element(self.driver.find_element(By.XPATH, self.contact_salutation)).click().perform()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.contact_salutation_option.format(salutation)).click()
            self.driver.find_element(By.XPATH, self.contact_first_name).send_keys(first_name)
            self.driver.find_element(By.XPATH, self.contact_last_name).send_keys(last_name)

            # Save the contact
            self.logger.info("Saving the contact")
            self.driver.find_element(By.XPATH, self.contact_or_opportunity_save_button).click()
            time.sleep(10)

            self.logger.info("contact saved successfully")

        except Exception as e:
            self.logger.error(f"An error occurred while creating a contact: {e}")
            self.driver.save_screenshot("create_contact_error.png")
            raise
    def verify_contact_has_saved(self, contact_name):
        # Verifying contact has saved
        element = self.driver.find_element(By.XPATH, self.verify_contact_or_opportunity.format(contact_name))  #Noya B
        return element.text
