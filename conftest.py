import pytest


@pytest.fixture(scope='class')
def pre_and_post_action(request):
    from selenium import webdriver
    driver = webdriver.Chrome(
        executable_path="C:/Users/Administrator/PycharmProjects/Automation_POM/drivers/chromedriver.exe")
    driver.get("http://localhost/login.do")
    driver.implicitly_wait(30)
    request.cls.driver = driver
