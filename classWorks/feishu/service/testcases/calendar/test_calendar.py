import pytest

from classWorks.feishu.service.testcases.calendar.base_calendars_testcase import BaseCalendarTestCase
from classWorks.feishu.service.utils import Utils


class TestCalendar(BaseCalendarTestCase):
  def setup_class(self):
    super().setup_class()

  @pytest.mark.parametrize("json_datas", Utils.load_yaml('../../datas/calendar/create.yaml', type="normal"))
  def test_create(self, json_datas):
    print(f"json_datas: {json_datas}")
    item = self.calendar.create(json_datas)
    print(item)
    # self.calendar.check_success(item)
    # item_list = self.calendar.list()
    # assert item in item_list