from classWorks.feishu1.service.api.base_api import BaseApi


class FeiShuApi(BaseApi):
  def __init__(self):
    super().__init__()
    self.token = self.get_tenant_access_token()
    self.req.headers = {"Content-Type": "application/json; charset=utf-8"}
    self.req.headers["Authorization"] = f"Bearer {self.token}"


  def get_tenant_access_token(self):
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    json = {
      "app_id": "cli_a074306e80f9900b",
      "app_secret": "639fuGSezXKEER2ZtA1IbgT1suWqiD86"
    }
    res = self.req.post(url, json=json)
    code = res.json()["code"]
    expire = res.json()["expire"]
    if expire == 0:
      raise ConnectionError("秘钥过期了，请更新")
    elif code != 0:
      raise ConnectionError(f"current_code: {code}, expire_code: 0")
    # print(res.json())
    return res.json()["tenant_access_token"]

  def check_success(self, res, type='code', expire=0):
    assert res[type] == expire

  def check_error(self, res, type='code', expire=0):
    assert res[type] != expire

if __name__ == "__main__":
  feishu_base_api = FeiShuApi()
  print(feishu_base_api.get_tenant_access_token())
  print(feishu_base_api.req.headers)