import random

import allure
import pytest
import json

from classWorks.feishu1.service.testcase.calendars.base_calendars_testcase import BaseCalendarsTestCase
from classWorks.feishu1.service.utils import Utils

list_normal_data = Utils.yaml_load("../../data/list.yaml", "normal")
create_normal_data = Utils.yaml_load("../../data/create.yaml", "normal")
update_normal_data = Utils.yaml_load("../../data/update.yaml", "normal")

@allure.feature('日历功能')
class TestCalendars(BaseCalendarsTestCase):
  def setup(self):
    self.calendar_id = []

  @allure.story('创建日历')
  @pytest.mark.parametrize("data", create_normal_data["datas"], ids=create_normal_data["ids"])
  def test_create(self, data):
    with allure.step("创建日历"):
      res = self.calendarsApiHttp.create(data)
    with allure.step("校验方式一：通过响应码code"):
      self.calendarsApiHttp.check_success(res)
    with allure.step("获取日历列表"):
      item_list_res = self.calendarsApiHttp.list()
      item_list = item_list_res["data"]["calendar_list"]
    with allure.step("获取创建的日历"):
      item = res["data"]["calendar"]
    with allure.step("检验方式二：判断创建日历是否在列表中"):
      item_list.index(item)

  @pytest.mark.parametrize("data", list_normal_data)
  def test_list(self, data):
    res = self.calendarsApiHttp.list(data)
    self.calendarsApiHttp.check_success(res)

  @pytest.mark.parametrize("data", create_normal_data["datas"])
  def test_delete(self, data):
    calendar_list = self.calendarsApiHttp.list()["data"]["calendar_list"]
    if len(calendar_list) != 0:
      index = random.randint(0, len(calendar_list))
      self.calendar_id.append(calendar_list[index]["calendar_id"])
    else:
      res = self.calendarsApiHttp.create(data[0])
      self.calendar_id.append(res["data"]["calendar"]["calendar_id"])
    res = self.calendarsApiHttp.delete(self.calendar_id[0])
    self.calendarsApiHttp.check_success(res)

  @pytest.mark.parametrize("create_data", create_normal_data["datas"])
  @pytest.mark.parametrize("update_data", update_normal_data["datas"])
  def test_update(self, create_data, update_data):
    calendar_list = self.calendarsApiHttp.list()["data"]["calendar_list"]
    if len(calendar_list) != 0:
      index = random.randint(0, len(calendar_list))
      self.calendar_id.append(calendar_list[index]["calendar_id"])
    else:
      res = self.calendarsApiHttp.create(create_data[0])
      self.calendar_id.append(res["data"]["calendar"]["calendar_id"])
    update_data["id"] = self.calendar_id[0]
    res = self.calendarsApiHttp.update(update_data)
    self.calendarsApiHttp.check_success(res)
    item_list_res = self.calendarsApiHttp.list()
    item_list = item_list_res["data"]["calendar_list"]
    item = res["data"]["calendar"]
    item_list.index(item)