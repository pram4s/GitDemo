from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getlogger()
        homepage = HomePage(self.driver)

        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # homepage.shopitems().click() is replaced by below as the object in HomePage is handling the click
        checkoutpage = homepage.shopitems()
        log.info("Products are loaded")
        # checkoutpage = CheckOutPage(self.driver) is removed as object creation is moved to HomePage
        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        products = checkoutpage.getproducts()
        for product in products:
            productname = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productname + " will be selected")
            if productname == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkoutpage.getcheckout().click()

        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        # checkoutpage.getfinalcheckout().click() is replaced by below as the object in CheckoutPage
        # is handling the click
        confirmpage = checkoutpage.getfinalcheckout()

        # confirmpage = ConfirmPage(self.driver) is removed as object creation is moved to CheckoutPage
        # self.driver.find_element(By.ID, "country").send_keys("Ind")
        confirmpage.getlocation().send_keys("Ind")
        # explicit wait is moved to BaseClass and below like is added for same
        self.verifylinkpresence("India", 10)

        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmpage.getvalue().click()

        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmpage.getterms().click()

        # self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        confirmpage.getpurchasebutton().click()

        # successtext = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        successtext = confirmpage.getmessage().text
        assert "Success! Thank you!" in successtext
