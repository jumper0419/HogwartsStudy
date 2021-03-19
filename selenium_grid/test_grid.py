import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestGrid:
  def setup(self):
    hub_url = "http://localhost:4444/wd/hub"
    caps = DesiredCapabilities.CHROME.copy()
    self.driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=caps)
    self.driver.implicitly_wait(5)

  def teardown(self):
    self.driver.quit()

  def test_grid(self):
    for i in range(4):
      self.driver.get("http://www.baidu.com")
      self.driver.find_element_by_id('kw').send_keys("nihao")
      self.driver.find_element_by_id("su").click()
      time.sleep(3)

