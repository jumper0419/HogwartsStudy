from classWorks.feishu1.web.page.feishu_index_page import FeiShuIndexPage


class BaseFeiShuTestCase:
  def setup_class(self):
    self.feishu_index_page = FeiShuIndexPage()