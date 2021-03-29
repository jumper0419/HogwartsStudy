import requests


class Base:
  def __init__(self):
    self.s = requests.Session()
    self.token = self.get_token()
    self.s.params = {'access_token': self.token}

  def get_token(self):
    params = {
      "corpid": "wwbad16854bf5f5a0f",
      "corpsecret": "nhEWxGWujJDc130dJU68EpzpeXavfGE-9nInnSVfW6Q"
    }

    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    res = self.s.get(url, params=params)
    return res.json()["access_token"]

  def send(self, *args, **kwargs):
    return self.s.request(*args, **kwargs)









