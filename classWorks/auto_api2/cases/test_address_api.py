import pytest
import yaml

from classWorks.auto_api2.api.address_api import AddressApi

members = yaml.safe_load(open('../data/member.yml', encoding='utf-8'))

class TestAddressApi:

  def setup_class(self):
    self.address = AddressApi()

  # 数据清理
  def setup(self, members=members):
    for member in members:
      self.address.delete_member(member["userid"])

  # 数据恢复
  def teardown(self, members=members):
    for member in members:
      self.address.delete_member(member["userid"])

  # 测试得到的成员名字是否一致
  @pytest.mark.parametrize('member', members)
  def test_get_member_info(self, member):
    # 测试前提
    self.address.create_member(**member)
    # 得到成员
    result = self.address.get_member_info(member['userid'])
    # 判断
    assert result["name"] == member["name"]

  @pytest.mark.parametrize("member", members)
  def test_create_member(self, member):
    result = self.address.create_member(**member)
    assert result["errmsg"] == "created"

  @pytest.mark.parametrize("member", members)
  def test_update_member(self, member):
    # 测试前提
    self.address.create_member(**member)
    member["name"] = member["name"] + "_tmp"
    result = self.address.update_member(userid=member["userid"], name=member["name"])
    assert result["errcode"] == 0
    assert result["errmsg"] == "updated"

  @pytest.mark.parametrize("member", members)
  def test_delete_member(self, member):
    # 测试前提
    self.address.create_member(**member)

    result = self.address.delete_member(member["userid"])
    assert result["errmsg"] == "deleted"

  def test_data(self):
    data = yaml.safe_load(open('../data/member.yml', encoding='utf-8'))
    print(data)
    for item in data:
      print(item["userid"], type(item["userid"]))