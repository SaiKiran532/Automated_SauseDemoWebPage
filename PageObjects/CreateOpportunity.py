import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Locators.Locators import Locators

class CreateOpportunity(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def create_opportunity(self, op_name):
        try:
            action = ActionChains(self.driver)
            # Fill out the opportunity form
            action.move_to_element(self.driver.find_element(By.XPATH, self.new_opportunity)).click().perform()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.opportunity_name).clear()
            self.driver.find_element(By.XPATH, self.opportunity_name).send_keys(op_name)
            # Save the contact
            self.logger.info("Saving the contact")
            self.driver.find_element(By.XPATH, self.contact_or_opportunity_save_button).click()
            time.sleep(10)

            self.logger.info("opportunity saved successfully")

        except Exception as e:
            self.logger.error(f"An error occurred while creating a opportunity: {e}")
            self.driver.save_screenshot("create_opportunity_error.png")
            raise
    def verify_opportunity_has_saved(self, opportunity_name):
        # Verifying opportunity has saved
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.verify_contact_or_opportunity.format(opportunity_name))
        action.scroll_to_element(element)
        return element.text
