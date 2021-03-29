import json

from classWorks.auto_api2.api.base import Base


class AddressApi(Base):

  def get_member_info(self, userid: str):
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
    params = {
      "access_token": self.token,
      "userid": userid
    }
    res = self.send('GET', url, params=params)
    return res.json()

  def create_member(self, userid: str = '', name: str = '', mobile: str = '', department: list = []):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
    data = {
      "userid": userid,
      "name": name,
      "mobile": mobile,
      "department": department
    }
    res = self.send('POST', url, json=data)
    return res.json()

  def update_member(self, userid: str = '', name: str = ''):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
    data = {
      'userid': userid,
      'name': name
    }
    res = self.send('POST', url, data=json.dumps(data))
    return res.json()

  def delete_member(self, userid: str):
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
    params = {
      "access_token": self.token,
      "userid": userid
    }
    res = self.send('GET', url, params=params)
    return res.json()

