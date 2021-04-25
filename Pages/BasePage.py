import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class base:
    def __init__(self, driver):
        self.driver = driver

    def doClick(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.click()

    def do_Send_Keys(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(text)

    def do_Clear(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.clear()

    def do_Select(self, by_locator, text):
        drp = Select(self.driver.find_element_by_id(by_locator))
        drp.select_by_visible_text(text)

    def do_ScrollByPixel(self, by_locator):
        self.driver.execute_script('window.scrollBy(0,500)', '')

    def do_Hover(self, by_locator1, by_locator2):
        time.sleep(3)
        element1 = self.driver.find_element_by_xpath(by_locator1)
        element2 = self.driver.find_element_by_xpath(by_locator2)
        action = ActionChains(self.driver)
        action.move_to_element(element1).move_to_element(element2).click().perform()
    def get_Title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_contains(title))
        return self.driver.title

