from classWorks.feishu.service.api.feishuApi import FeiShuApi


class CalendarApi(FeiShuApi):
  """
  日历管理：calendars api的统一设置，比如url前缀、日志的创建、删除、更新、获取
  """
  BASE_URL = "https://open.feishu.cn/open-apis/calendar/v4/calendars"


  def create(self, name: object):
    """
    创建某一个日历
    :param name: 日历名称
    :return:
    """
    print(f"CalendarApi_token: {super().token}")
    print(f"Auth: {self.headers['Authorization']}")
    pass

  def list(self):
    """
    获取所有日历
    :return:
    """
    pass

  def get(self, id):
    """
    获取某一个具体日历
    :param id: 日历id
    :return:
    """
    pass

  def delete(self, id):
    """
    删除某一个具体日历
    :param id: 日历id
    :return:
    """
    pass

  def update(self, **kwargs):
    """
    更新某个日历
    :param kwargs: 更新参数
    :return:
    """
    pass
