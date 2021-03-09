# -*- encoding: UTF-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appAuto.studycases.base_browser import Base


class TestApp(Base):
    def test_fist_app(self):
        sleep(1)
        self.driver.get("http://www.baidu.com")
        search_locator = (By.CSS_SELECTOR, "#index-kw")
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(search_locator))
        self.driver.find_element(*search_locator).click()
        self.driver.find_element(*search_locator).send_keys("我是共产党")
        # sug_locator = (By.XPATH, "//*[@class='sug']/button")
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(sug_locator))
        # self.driver.find_element(*sug_locator).click()
        self.driver.find_element(By.CSS_SELECTOR, "#index-bn").click()
        sleep(3)
        # self.driver.find_element_by_xpath("//*[@id='userinfo-wrap']//a").click()