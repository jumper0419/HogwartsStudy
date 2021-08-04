from classWorks.feishu1.web.testcase.base_feishu_testcase import BaseFeiShuTestCase


class TestCalendars(BaseFeiShuTestCase):
  def setup(self):
    self.calendar = self.feishu_index_page.goto_calendar()

  def test_create(self):
    print(self.calendar)