from random import random
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self, driver, username="", phone="", acctid=""):
        self.driver = driver
        self.username = username
        self.phone = phone
        self.acctid = acctid

    def add_member(self):
        def wait_add(driver):
            sleep(1)
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
            # print(len(eles))
            eles[1].click()
            save_eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']")
            return len(save_eles) >= 1

        WebDriverWait(self.driver, 10).until(wait_add)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_css_selector('#memberAdd_acctid').send_keys(self.acctid+int(random()*100))
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys(self.phone+int(random()*100))
        self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']")[0].click()


