from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.ID, "country")
    location = (By.ID, "country")

    # driver.find_element(By.LINK_TEXT, "India")
    value = (By.LINK_TEXT, "India")

    # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    terms = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    # driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    purchasebutton = (By.CSS_SELECTOR, "input[type='submit']")

    # driver.find_element(By.CLASS_NAME, "alert-success")
    message = (By.CLASS_NAME, "alert-success")

    def getlocation(self):
        return self.driver.find_element(*ConfirmPage.location)

    def getvalue(self):
        return self.driver.find_element(*ConfirmPage.value)

    def getterms(self):
        return self.driver.find_element(*ConfirmPage.terms)

    def getpurchasebutton(self):
        return self.driver.find_element(*ConfirmPage.purchasebutton)

    def getmessage(self):
        return self.driver.find_element(*ConfirmPage.message)