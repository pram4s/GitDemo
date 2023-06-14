from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    products = (By.XPATH, "//div[@class='card h-100']")

    # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    finalcheckout = (By.XPATH, "//button[@class='btn btn-success']")

    def getproducts(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def getcheckout(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def getfinalcheckout(self):
        self.driver.find_element(*CheckOutPage.finalcheckout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
