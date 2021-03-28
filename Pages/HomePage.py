from selenium.webdriver.common.by import By

from Pages.AdvancedSearch import AdvancedSearch
from Pages.BasePage import base
import pytest


class HomePage(base):
    bttn_UpdateProfile = (By.XPATH, "//div[text()='UPDATE PROFILE']")
    bttn_FileUpload = (By.XPATH, "//*[@type='button' and @value='Update Resume']")
    bttn_Jobs = "/html/body/div[1]/div/div/ul[1]/li[1]/a"
    bttn_AdvancedSearch = "/html/body/div[1]/div/div/ul[1]/li[1]/div/ul[1]/li[2]/a"
    bttn_CreateFreeJobAlert = "/html/body/div[1]/div/div/ul[1]/li[1]/div/ul[1]/li[3]/a"

    def __init__(self, driver):
        super().__init__(driver)

    '''def doUpload(self, fpath):
        self.doClick(self.bttn_UpdateProfile)
        self.do_ScrollByPixel(self.bttn_FileUpload)
        self.do_Send_Keys(self.bttn_FileUpload, fpath)'''
    def getTitle(self, title):
        return self.get_Title(title)

    def doAdvancedSearch(self):
        self.do_Hover(self.bttn_Jobs, self.bttn_AdvancedSearch)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        #return AdvancedSearch(self.driver)
