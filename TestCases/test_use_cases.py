import time

import pytest

from PageObjects.ConvertLead import ConvertLead
from PageObjects.CreateContact import CreateContact
from PageObjects.CreateLead import CreateLead
from PageObjects.CreateOpportunity import CreateOpportunity
from PageObjects.LoginPage import LoginPage
from PageObjects.RemoveAccount import RemoveAccount
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Testcase001:
    pageurl = ReadConfig.get_Application_url()
    username = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    project_root = os.path.dirname(os.path.abspath(__file__))
    screenshot_folder = os.path.join(project_root, "Screenshots")
    screenshot_path = os.path.join(screenshot_folder, "test_homepage_title.png")

    def test_salesforce_page_title(self, setup):
        self.logger.info("********** Testcase001 ********** ")
        self.logger.info("********** Verifying Homepage Title **********")

        self.driver = setup
        self.driver.get(self.pageurl)
        time.sleep(2)
        actual_title1 = self.driver.title
        if actual_title1 == "Login | Salesforce":
            assert True
            self.logger.info("********** Homepage title test passed **********")
        else:
            self.driver.save_screenshot(self.screenshot_path)
            self.logger.error("********** Homepage title test failed **********")
            assert False

    def test_user_login_into_salesforce(self, setup):
        self.logger.info("********** Login testcase started **********")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("********** Login testcase ended **********")

    @pytest.mark.parametrize("salutation, first_name, last_name, company", [
        ("Mr.", "Robert", "Twin", "Acme Corp")
    ])
    def test_create_lead(self, salutation, first_name, last_name, company,setup):
        self.driver = setup
        self.cl = CreateLead(self.driver)
        self.cl.create_lead(salutation, first_name, last_name, company)
        self.logger.info(f"Lead created: {first_name} {last_name}, {company}")
        self.logger.info(f"Verifying lead has created")
        text = self.cl.verify_lead_has_created()
        if text == "Mr. Robert Twin":
            assert True
            self.logger.info("********** Lead has successfully created and verified **********")
        else:
            self.driver.save_screenshot(self.screenshot_path)
            self.logger.error("********** Failed in verifying lead **********")
            assert False

    def test_convert_lead(self,setup):
        self.driver = setup
        self.rl = ConvertLead(self.driver)
        self.rl.convert_lead()
        self.logger.info(f"Lead Converted")

        text = self.rl.verify_lead_has_converted()
        if text == "Your lead has been converted":
            assert True
            self.logger.info("********** Lead has successfully created and verified **********")
        else:
            self.driver.save_screenshot(self.screenshot_path)
            self.logger.error("********** Failed in verifying lead **********")
            assert False

        self.rl.go_to_leads_page()

    @pytest.mark.parametrize("salutation, first_name, last_name, existing_contact,contact_name", [
        ("Mr.", "Noya", "B", "Acme Corp", "Noya B")
    ])
    def test_create_contact(self,salutation,first_name,last_name,existing_contact,contact_name,setup):
        self.driver = setup
        self.cc = CreateContact(self.driver)
        self.cc.create_contact(salutation,first_name,last_name,existing_contact)
        self.logger.info(f"Contact created")

        text = self.cc.verify_contact_has_saved(contact_name,existing_contact)
        if text == "Noya B":
            assert True
            self.logger.info("********** Contact has successfully created and verified **********")
        else:
            self.driver.save_screenshot(self.screenshot_path)
            self.logger.error("********** Failed in verifying Contact **********")
            assert False

    @pytest.mark.parametrize("opportunity_name,existing_contact,close_date,stage,forecast_category", [
        ("Zaya Opp","Acme Corp","02/2/2025","Propose","Pipeline")
    ])
    def test_create_opportunity(self,opportunity_name,existing_contact,close_date,stage,forecast_category,setup):
        self.driver = setup
        self.cp = CreateOpportunity(self.driver)
        self.cp.create_opportunity(opportunity_name,existing_contact,close_date,stage,forecast_category)
        self.logger.info(f"Opportunity created")

        text = self.cp.verify_opportunity_has_saved(opportunity_name,existing_contact)
        if text == "Zaya Opp":
            assert True
            self.logger.info("********** Opportunity has successfully created and verified **********")
        else:
            self.driver.save_screenshot(self.screenshot_path)
            self.logger.error("********** Failed in verifying Opportunity **********")
            assert False


    def test_remove_account(self,setup):
        self.driver = setup
        self.rc = RemoveAccount(self.driver)
        self.rc.remove_account()
        self.logger.info(f"Account Removed Successfully")


    def test_loggout_from_Sales_force(self,setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.click_logout()
        self.logger.info(f"Logged out Successfully")

