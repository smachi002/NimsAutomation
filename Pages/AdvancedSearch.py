from selenium.webdriver.common.by import By

from Pages.BasePage import base


class AdvancedSearch(base):
    txt_KeySkills = (By.XPATH, '//*[@name="qp"]')
    drp_Category = '//*[@id="0"]'
    txt_Location = (By.XPATH, '//*[@id="Sug_advLocation"]')
    def __init__(self, driver):
        super().__init__(driver)

    def doSearch(self, Skills, Location, Value):
        self.do_Send_Keys(self.txt_KeySkills, Skills)
        self.do_Select(self.drp_Category, Value)
        self.do_Send_Keys(self.txt_Location, Location)

