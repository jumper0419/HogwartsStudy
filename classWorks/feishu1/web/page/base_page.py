from appium.webdriver.webdriver import WebDriver
from selenium import webdriver

from classWorks.feishu1.web.utils import Utils


class BasePage:
  """
  通用功能
  """

  def __init__(self, driver:WebDriver=None):
      self.driver = webdriver.Chrome()
      self.driver.implicitly_wait(5)

  # @Utils.handle_blacklist
  def find(self, locator, value):
    return self.driver.find_element(locator, value)

  # @Utils.handle_blacklist
  def finds(self, locator, value):
    return self.driver.find_elements(locator, value)

  # @Utils.handle_blacklist
  def find_and_click(self, locator, value):
    return self.driver.find_element(locator, value).click()

  # @Utils.handle_blacklist
  def find_and_send(self, locator, value, text):
    return self.driver.find_element(locator, value).send_keys(text)

  def screenshot(self):
    return self.driver.get_screenshot_as_png()

