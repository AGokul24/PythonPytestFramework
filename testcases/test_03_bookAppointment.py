import json
import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AppointmentPage import AppointmentPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from datetime import datetime

class Test_003_BookAppointment:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.LogGeneration()
    # Import Json elements
    with open('C:/Users/Gokul A/PycharmProjects/pythonPytestFrameworkPOM/TestData/ApptData.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    indexOfDropdown = str(obj['indexOfDropdown'])
    # Get current date
    now = datetime.now()
    visitDate = now.strftime("%d-%m-%Y")
    comment = str(obj['comment'])

    def test_BookAppointment(self, setup):
        self.logger.info("******************** Test_003_BookAppointment ***********************")
        self.logger.info("******************** Booking an appointment ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #Login
        ObjectLogin = LoginPage(self.driver)
        ObjectLogin.setUserName(self.username)
        ObjectLogin.setPassword(self.password)
        ObjectLogin.clickLogin()
        time.sleep(3)
        #Book Appointment
        ObjectHomePage = AppointmentPage(self.driver)
        ObjectHomePage.dropdownOptionSelect(self.indexOfDropdown)
        ObjectHomePage.medicaidRadioSelection()
        ObjectHomePage.visitDateOfPatient(self.visitDate)
        ObjectHomePage.appointmentComments(self.comment)
        ObjectHomePage.bookAppointmentBtn()
        # Verification
        time.sleep(2)
        if self.comment == ObjectHomePage.commentCheckVerify():
            self.logger.info("******************** Appointment booked successfully ***********************")
            #Logout
            ObjectLogin.clickToggleBtn()
            ObjectLogin.clickLogoutBtn()
            ObjectLogin.ClickMakeAppointmentBtn()
            self.driver.close()
            assert True
        else:
            self.logger.error("******************** Unable to book an appointment ***********************")
            # Logout
            ObjectLogin.clickToggleBtn()
            ObjectLogin.clickLogoutBtn()
            ObjectLogin.ClickMakeAppointmentBtn()
            self.driver.close()
            assert False
