import pytest
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_form_submission(self, getdata):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        log.info("Entering " + getdata["firstname"] + " as First Name")
        # driver.find_element(By.NAME, "name").send_keys("Hello")
        # homepage.getname().send_keys(getdata[0])  # if tuple is used for data
        homepage.getname().send_keys(getdata["firstname"])  # if dictionary is used for data
        # driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        homepage.getemail().send_keys(getdata["email"])
        # driver.find_element(By.ID, "exampleInputPassword1").send_keys("Abc@123")
        # homepage.getpassword().send_keys("Abc@123")
        # driver.find_element(By.ID, "exampleCheck1").click()
        homepage.getcheckbox().click()
        # dd = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # gender selection moved to BaseClass and below line added
        self.selectoptionbytext(homepage.getgender(), getdata["gender"])
        # driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
        # homepage.getemployment().click()
        # driver.find_element(By.NAME, "bday").send_keys("23-05-2013")
        # homepage.getdob().send_keys("23-05-2013")
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(" World")
        # homepage.gettwoway().send_keys(" World")
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        homepage.getsubmit().click()
        # time.sleep(10)
        # message = driver.find_element(By.CLASS_NAME, "alert-success").text
        message = homepage.getsuccessmsg().text
        print(message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.gettestdata("testcase2"))
    # (params=HomePageData.test_homepage_data)
    def getdata(self, request):
        return request.param
