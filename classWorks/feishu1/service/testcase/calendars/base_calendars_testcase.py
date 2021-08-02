from classWorks.feishu1.service.api.calendars.calendars_api_http import CalendarsApiHttp
from classWorks.feishu1.service.testcase.base_feishu_testcase import BaseFeiShuTestCase

class BaseCalendarsTestCase(BaseFeiShuTestCase):
  def setup_class(self):
    self.calendarsApiHttp = CalendarsApiHttp()

  def setup(self):
    """
    清理数据
    :return:
    """
    pass

  def teardown(self):
    """
    清理数据，还原环境
    :return:
    """