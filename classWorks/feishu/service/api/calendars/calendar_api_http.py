from classWorks.feishu.service.api.calendars.calendar_api import CalendarApi


class CalendarApiHttp(CalendarApi):

  def create(self, name: object):
    print(self.token)
    print(type(name), name)
    data = {'summary': 'this is a test', 'description': '使用开放接口创建日历', 'permissions': 'public', 'color': 255, 'summary_alias': '日历备注名'}
    res = self.send_request('post', self.BASE_URL, json=data)
    print(res.json())
    return res.json()

