from classWorks.feishu.service.api.base_api import BaseApi


class FeiShuApi(BaseApi):
  """
  所有模块包都具有的功能：获取token， 获取身份信息，断言状态码200或者msg
  """
  def __int__(self):
    super().__init__()
    self.token: str = self.get_token()
    self.req.headers = {"Content-Type": "application/json; charset=utf-8"}
    self.req.headers["Authorization"] = f"Bearer {self.token}"

  def get_token(self, _type: str="tenant", internal=True):
    """
    获取token
    :param types: 获取token的方式， 默认为企业级，例如：['app', 'tenant']
    :param internal: 是企业自建还是商店应用，默认为企业自建
    :return:
    """
    BASE_URL = "https://open.feishu.cn/open-apis/auth/v3/"
    _type += "_access_token"
    type_list = ["app_access_token", "tenant_access_token"]
    if _type in type_list and internal == False:
      url = BASE_URL + _type + "/"
    elif _type in type_list and internal == True:
      url = BASE_URL + _type + "/internal/"
    else:
      raise TypeError(f"获取token失败，没有这样的type：{_type}, expire_type: {type_list}")

    json_datas = {
      "app_id": "cli_a074306e80f9900b",
      "app_secret": "639fuGSezXKEER2ZtA1IbgT1suWqiD86"
    }
    res = self.send_request('post', url, json=json_datas)
    # print(res.json())
    # return
    code = res.json()["code"]
    expire = res.json()["expire"]
    if expire == 0:
      raise ConnectionError("秘钥过期了，请更新")
    elif code != 0:
      raise ConnectionError(f"current_code: {code}, expire_code: 0")
    else:
      print("sss", self.req.headers)
      return res.json()[_type]

  def check_success(self, res, type: str="code", expire=200):
    assert res[type] == expire

if __name__ == "__main__":
  fs = FeiShuApi()
  print(fs.token)
