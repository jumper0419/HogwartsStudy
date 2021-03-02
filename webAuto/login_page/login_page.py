from selenium.webdriver.common.by import By

from webAuto.login_page.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # TODO:
    def scan(self):
        return "暂时没有实现扫码功能"


    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()
        return RegisterPage(self.driver)
