from time import sleep

from selenium.webdriver.common.by import By

from classWorks.feishu1.web.page.base_page import BasePage


class FeiShuIndexPage(BasePage):
  """
  与飞书通用业务相关的功能
  """

  def __init__(self):
    super().__init__()
    self.BASE_URL = "https://test-cd2zqom0lzee.feishu.cn/admin/"
    self.driver.get(f"{self.BASE_URL}index")

  def goto_calendar(self):
    sleep(3)
    print(self.BASE_URL)
    print(f"{self.BASE_URL}index")
    self.find_and_click(By.XPATH, "//*[@text='全员日历']")


