import requests


class BaseApi:
  """
  封装requests等库的细节， 实现与具体的请求工具无关，以及简化一些操作
  """
  def __init__(self):
    self.req = requests.Session()

  def send_request(self, *args, **kwargs):
    return self.req.request(*args, **kwargs)

  def json(self):
    """
    将结果转成json对象
    :return:
    """
    pass
