import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class CalendarsPage:
  def setup(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(5)
    self.driver.get("https://test-cd2zqom0lzee.feishu.cn/admin/index")

  def goto_calendars(self):
    time.sleep(3)
    ele = self.driver.find_element(By.XPATH, "//*[@text='全员日历']")
    ele.click()
