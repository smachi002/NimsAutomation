import allure
from allure_commons.types import AttachmentType
from Pages.LoginPage import LoginPage
from TestCases.BaseTest import BaseTest
from Utility.readProperties import cnfParser
from Configuration.Conftest import setup
import pytest


class TestLogin(BaseTest):
    Email = cnfParser.getEmail()
    Password = cnfParser.getPassword()

    #@allure.severity(allure.severity_level.BLOCKER)
    #@pytest.mark.sanity
    def test_Login(self):
        self.lp = LoginPage(self.driver)
        self.lp.doLogin(self.Email, self.Password)
        #allure.attach(self.driver.get_screenshot_as_png(), name="TestCaseLogin", attachment_type=AttachmentType.PNG)
        #HomePage = self.lp.doLogin(self.Email, self.Password)
