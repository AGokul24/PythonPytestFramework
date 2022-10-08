import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities import ExcelUtils
from utilities.customLogger import LogGen

class Test_002_Login_DataDriven:
    baseUrl = ReadConfig.getApplicationURL()
    try:
        path = ".//TestData/LoginDDT.xlsx"
    except FileNotFoundError:
        print("Excel file is directory is not recognized")
    logger = LogGen.LogGeneration()
    list_status = []

    def test_login_datadriven(self, setup):
        self.logger.info("******************** Test_002_Login_DataDriven ***********************")
        self.logger.info("******************** Verifying the login Data Driven test ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        ObjectLogin = LoginPage(self.driver)
        #Get the maximum row count
        totalRows = ExcelUtils.getRowCount(self.path, "Sheet1")
        print("Total number of rows in the excel : "+str(totalRows))

        for r in range (2, totalRows+1):
            usernameXL = ExcelUtils.readData(self.path, "Sheet1", r, 1)
            passwordXL = ExcelUtils.readData(self.path, "Sheet1", r, 2)
            expectedResultXL = ExcelUtils.readData(self.path, "Sheet1", r, 3)
            ObjectLogin.setUserName(usernameXL)
            ObjectLogin.setPassword(passwordXL)
            ObjectLogin.clickLogin()
            #verification
            actual_title = self.driver.title
            if actual_title == 'CURA Healthcare Service':
                if expectedResultXL == 'Pass':
                    self.logger.info("******************** Login Passed - Correct user credentials ***********************")
                    ObjectLogin.clickToggleBtn()
                    ObjectLogin.clickLogoutBtn()
                    ObjectLogin.ClickMakeAppointmentBtn()
                    self.list_status.append("Pass")
                elif expectedResultXL == 'Fail':
                    self.logger.info("******************** Login Failed - Incorrect user credentials ***********************")
                    self.list_status.append("Pass")
        # Verification
        if "Fail" not in self.list_status:
            self.logger.info("******************** Login Data Driven test is passed ***********************")
            self.driver.close()
            assert True
        else:
            self.logger.info("******************** Login Data Driven test is failed ***********************")
            self.driver.close()
            assert False
        self.logger.info("******************** Completed Test_002_Login_DataDriven testcase ***********************")

