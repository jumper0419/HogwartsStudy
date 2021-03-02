from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self, driver, username="", phone="", acctid=""):
        self.driver = driver
        self.username = username
        self.phone = phone
        self.acctid = acctid

    def goto_add_member(self):
        def wait_add(driver):
            eles = driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')
            eles[-1].click()
            add_eles = driver.find_elements(By.XPATH, "//*[@id='memberAdd_acctid']")
            return len(add_eles) >= 1

        WebDriverWait(self.driver, 30).until(wait_add)
        # self.driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')[-1].click()
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_css_selector('#memberAdd_acctid').send_keys(self.acctid)
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys(self.phone)
        self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']")[0].click()