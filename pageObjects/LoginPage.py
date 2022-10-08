from selenium.webdriver.common.by import By

class LoginPage():
    textbox_username_id = "txt-username"
    textbox_password_id = "txt-password"
    login_btn_xpath = "//button[@id='btn-login']"
    toggleMenuIcon_xpath = "//a[@id='menu-toggle']"
    logout_xpath = "//a[contains(text(),'Logout')]"
    MakeAppointment_xpath = "//h2[contains(text(),'Make Appointment')]"
    MakeAppointmentBtn_xpath = "//a[@id='btn-make-appointment']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def clickToggleBtn(self):
        self.driver.find_element(By.XPATH, self.toggleMenuIcon_xpath).click()

    def clickLogoutBtn(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

    def ClickMakeAppointmentBtn(self):
        self.driver.find_element(By.XPATH, self.MakeAppointmentBtn_xpath).click()

