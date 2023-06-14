from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # for test_e2e
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    # for test_HomePage
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    employment = (By.CSS_SELECTOR, "#inlineRadio2")
    dob = (By.NAME, "bday")
    twoway = (By.XPATH, "(//input[@type='text'])[3]")
    submit = (By.XPATH, "//input[@type='submit']")
    successmsg = (By.CLASS_NAME, "alert-success")

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getemployment(self):
        return self.driver.find_element(*HomePage.employment)

    def getdob(self):
        return self.driver.find_element(*HomePage.dob)

    def gettwoway(self):
        return self.driver.find_element(*HomePage.twoway)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getsuccessmsg(self):
        return self.driver.find_element(*HomePage.successmsg)
