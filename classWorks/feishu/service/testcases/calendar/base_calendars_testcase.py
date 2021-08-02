from classWorks.feishu.service.testcases.base_feishu_testcase import BaseFeiShuTestCase
from classWorks.feishu1.service.api.calendars.calendars_api_http import CalendarsApiHttp


class BaseCalendarTestCase(BaseFeiShuTestCase):

  def setup_class(self):
    self.calendars_api_http = CalendarsApiHttp()