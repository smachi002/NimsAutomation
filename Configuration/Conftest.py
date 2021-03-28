from selenium import webdriver
import pytest


@pytest.fixture(params=['chrome'], scope='class')
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver

    yield
    driver.quit()

