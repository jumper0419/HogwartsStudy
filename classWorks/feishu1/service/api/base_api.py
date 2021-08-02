import requests
import yaml


class BaseApi:
  def __init__(self):
    self.req = requests.Session()

  def send_request(self, *args, **kwargs):
    return self.req.request(*args, **kwargs)




if __name__ == "__main__":
  base = BaseApi()
  print(base.get_datas("../data/create.yaml", "normal"))
