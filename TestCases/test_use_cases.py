import time

import pytest

from PageObjects.ConvertLead import ConvertLead
from PageObjects.CreateContact import CreateContact
from PageObjects.CreateLead import CreateLead
from PageObjects.CreateOpportunity import CreateOpportunity
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Testcase001:
    pageurl = ReadConfig.get_Application_url()
    username = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    scree_shot_path = "C:\\Users\\saikiran.challa\\PycharmProjects\\pythonProject5\\Screenshots\\test_homepage_title.png"

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
            self.driver.save_screenshot(self.scree_shot_path)
            self.logger.error("********** Homepage title test failed **********")
            assert False

    def test_user_login_into_salesforce(self, setup):
        self.logger.info("********** Login testcase started **********")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
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
            self.driver.save_screenshot(self.scree_shot_path)
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
            self.driver.save_screenshot(self.scree_shot_path)
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
        self.logger.info(f"Contact Saved")

        text = self.cc.verify_contact_has_saved(contact_name)
        if text == "Noya B":
            assert True
            self.logger.info("********** Lead has successfully created and verified **********")
        else:
            self.driver.save_screenshot(self.scree_shot_path)
            self.logger.error("********** Failed in verifying lead **********")
            assert False

    @pytest.mark.parametrize("opportunity_name", [
        ("Zaya Opp")
    ])
    def test_create_opportunity(self,opportunity_name,setup):
        self.driver = setup
        self.cp = CreateOpportunity(self.driver)
        self.cp.create_opportunity(opportunity_name)
        self.logger.info(f"Contact Saved")

        text = self.cp.verify_opportunity_has_saved(opportunity_name)
        if text == "Zaya Opp":
            assert True
            self.logger.info("********** Lead has successfully created and verified **********")
        else:
            self.driver.save_screenshot(self.scree_shot_path)
            self.logger.error("********** Failed in verifying lead **********")
            assert False