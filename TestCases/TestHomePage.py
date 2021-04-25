import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from TestCases.BaseTest import BaseTest
from Configuration.Conftest import setup

from Utility.readProperties import cnfParser


class TestHomePage(BaseTest):
    Email = cnfParser.getEmail()
    Password = cnfParser.getPassword()
    FilePath = "C:\\Data\\Swapnil Machikar_Automation_Resume.docx"
    homeTitle = 'Home | Mynaukri'


    '''def test_doUpload(self):
        self.lp = LoginPage(self.driver)
        homePage = self.lp.doLogin(self.Email, self.Password)
        homePage.doUpload(self.FilePath)'''

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_Title(self):
        self.lp = LoginPage(self.driver)
        self.lp.doLogin(self.Email, self.Password)
        homePage = HomePage(self.driver)
        Title = homePage.getTitle(self.homeTitle)
        allure.attach(self.driver.get_screenshot_as_png(), name="test_Title", attachment_type=AttachmentType.PNG)
        assert Title == self.homeTitle

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_Hover(self):
        self.lp = LoginPage(self.driver)
        self.lp.doLogin(self.Email, self.Password)
        homePage = HomePage(self.driver)
        homePage.doAdvancedSearch()
        allure.attach(self.driver.get_screenshot_as_png(), name="test_Hover", attachment_type=AttachmentType.PNG)
        #homePage = self.lp.doLogin(self.Email, self.Password)

