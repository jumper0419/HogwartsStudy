from classWorks.feishu1.service.api.feishu_api import FeiShuApi


class CalendarsApi(FeiShuApi):
  """
  日历管理：calendars api的统一设置，比如url前缀、日志的创建、删除、更新、获取
  """
  def __init__(self):
    super().__init__()
    self.pre_fix = "https://"
    self.host = "open.feishu.cn"
    self.path = "/open-apis/calendar/v4/calendars/"
    self.BASE_URL = f"{self.pre_fix}{self.host}{self.path}"

  def create(self, json):
    """
    创建日历
    :param json: 传入json对象
    :return:
    """
    pass

  def list(self, json):
    """
    获取所有日历
    :param json: 传入json对象
    :return:
    """
    pass

  def get(self, id):
    """
    获取某一条日历
    :param id: 日历id
    :return:
    """
    pass

  def delete(self, id):
    pass

  def update(self, **kwargs):
    pass

