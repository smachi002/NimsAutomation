from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from Pages.BasePage import base
from Pages.HomePage import HomePage
from Utility.readProperties import cnfParser
import pytest
import allure


class LoginPage(base):
    link_Login = (By.XPATH, '//*[@id="login_Layer"]/div')
    txt_Email = (By.XPATH, "//*[@type='text']//preceding::input[2]")
    txt_Password = (By.XPATH, "//*[@type='text']//preceding::input[5]")
    bttn_Login = (By.XPATH, "//button[text()='Login']")
    Url = cnfParser.getApplicationUrl()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.Url)
        self.driver.maximize_window()

    def doLogin(self, Email, Password):
        self.doClick(self.link_Login)
        self.do_Send_Keys(self.txt_Email, Email)
        self.do_Send_Keys(self.txt_Password, Password)
        self.doClick(self.bttn_Login)
        # return HomePage(self.driver)
