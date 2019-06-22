from pages.loginpage import LoginPage
from pages.Homepage import HomePage
import pytest
# Launch and Login to an app
@pytest.mark.usefixtures("pre_and_post_action")
class TestLogin:
    def test_actilogin(self):
        driver=self.driver
        lp = LoginPage(driver)
        lp.acti_login()

    def test_actilogout(self):
        driver = self.driver
        hp=HomePage(driver)
        hp.acti_logout()

    # acti_login
    # global driver
    # driver=webdriver.Chrome(executable_path="C:/Users/Administrator/PycharmProjects/Automation_POM/drivers/chromedriver.exe")
    # driver.get("http://localhost/login.do")
    # driver.implicitly_wait(30)
    # driver.find_element_by_id("username").send_keys("admin")
    # driver.find_element_by_name("pwd").send_keys("manager")
    # driver.find_element_by_xpath("//div[text()='Login ']").click()

# logout froom an app
# def test_logout():
#     driver.find_element_by_id("logoutLink").click()
