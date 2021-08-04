from classWorks.feishu1.web.all_test.calendars_page import CalendarsPage


class TestCalendars:
  def test_create(self):
    self.main_page = CalendarsPage()
    self.main_page.goto_calendars()