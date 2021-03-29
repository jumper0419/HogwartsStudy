import json

import requests


class TestApi:
  def setup(self):
    self.token = self.get_token()

  def get_token(self):
    corpid = "wwbad16854bf5f5a0f"
    corpsecret = "nhEWxGWujJDc130dJU68EpzpeXavfGE-9nInnSVfW6Q"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    res = requests.get(url)
    return res.json()["access_token"]

  def test_get_department_info(self):
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/list"
    params = {
      "access_token": self.token,
      "department_id": 1,
      "fetch_child": 1
    }
    with open('./response.txt', 'w', encoding='utf-8') as f:
      res = requests.get(url, params=params)
      # print(res.json())
      f.write(res.text)
      for item in res.json()["userlist"]:
        if item["name"] == "wangsan":
          assert item["department"][0] == 2
          assert item["mobile"] == "12324243434"

  def test_get_member_info(self):
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
    params = {
      "access_token": self.token,
      "userid": "kenan01"
    }
    res = requests.get(url, params=params)
    print(res.json())
    assert res.json()["name"] == "kenan01"

  def test_create_member(self):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
    data = {
      "userid": "kenan01",
      "name": "kenan",
      "mobile": "18676765656",
      "department": [1, 2]
    }
    res = requests.post(url, json=data)
    print(res.json())
    assert res.json()["errmsg"] == "created"


  def test_update_member(self):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
    data = {
      'userid': 'kenan01',
      'name': 'kenan01'
    }
    res = requests.post(url, data=json.dumps(data))
    print(res.json())
    assert res.json()["errcode"] == 0
    assert res.json()["errmsg"] == "updated"

  def test_delete_member(self):
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
    params = {
      "access_token": self.token,
      "userid": "kenan01"
    }
    res = requests.get(url, params)
    print(res.json())
    assert res.json()["errmsg"] == "deleted"