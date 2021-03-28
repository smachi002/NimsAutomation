import pytest

from Pages.AdvancedSearch import AdvancedSearch
from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Configuration.Conftest import setup
from Utility.readProperties import cnfParser
from Pages.LoginPage import LoginPage


class TestAdvancedSearch(BaseTest):
    Skills = 'Python'
    Location = 'Pune'
    Value = "Architecture, Interior Design"
    Email = cnfParser.getEmail()
    Password = cnfParser.getPassword()

    @pytest.mark.sanity
    def test_AdvSearch(self):
        self.lp = LoginPage(self.driver)
        self.lp.doLogin(self.Email, self.Password)
        self.homePage = HomePage(self.driver)
        self.homePage.doAdvancedSearch()
        self.advancedsearch = AdvancedSearch(self.driver)
        self.advancedsearch.doSearch(self.Skills, self.Location, self.Value)
        #homePage = self.lp.doLogin(self.Email, self.Password)
        #AdvancedSearch = homePage.doAdvancedSearch()
        #AdvancedSearch.doSearch(self.Skills, self.Location, self.Value)


