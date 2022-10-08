import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.LogGeneration()

    def test_webPageTitle(self, setup):
        self.logger.info("******************** Test_001_Login ***********************")
        self.logger.info("******************** Verifying the Homepage title ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        actual_title = self.driver.title
        if actual_title == "CURA Healthcae Service":
            self.logger.info("******************** Homepage title test is passed ***********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_webPageTitle.png")
            self.logger.error("******************** Homepage title test is failed ***********************")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("******************** Verifying the login test ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        ObjectLogin = LoginPage(self.driver)
        ObjectLogin.setUserName(self.username)
        ObjectLogin.setPassword(self.password)
        ObjectLogin.clickLogin()
        actual_title = self.driver.title
        if actual_title == "CURA Healthcare Service":
            self.logger.info("******************** Login test is passed ***********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("******************** Login test is failed ***********************")
            self.driver.close()
            assert False
        self.logger.info("******************** Completed Test_001_Login testcase ***********************")