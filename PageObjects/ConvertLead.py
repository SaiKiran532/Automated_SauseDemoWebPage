import logging
import time

from selenium.webdriver.common.by import By
from PageObjects.Locators.Locators import Locators
from selenium.webdriver import ActionChains


class ConvertLead(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def convert_lead(self):
        try:
            self.logger.info("Clicking the convert")
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element(By.XPATH, self.convert_button1)).click().perform()
            time.sleep(5)
            action.move_to_element(self.driver.find_element(By.XPATH, self.convert_button2)).click().perform()
            time.sleep(5)

            self.logger.info("Lead converted successfully")

        except Exception as e:
            self.logger.error(f"An error occurred while converting a lead: {e}")
            self.driver.save_screenshot("convert_lead_error.png")
            raise

    def verify_lead_has_converted(self):
        # Verifying lead has converted
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.lead_converted_verify)
        return element.text

    def go_to_leads_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.goto_leads)).click().perform()
        time.sleep(5)