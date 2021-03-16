from classWorks.ui_framework2.pages.base_page import BasePage
from classWorks.ui_framework2.pages.market_page import MarketPage


class MainPage(BasePage):

    def goto_market(self):
        self.parse_keywords("../datas/main_page.yml", 'goto_market')
        return MarketPage(self.driver)
