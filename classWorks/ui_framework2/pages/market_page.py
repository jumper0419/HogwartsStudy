from classWorks.ui_framework2.pages.base_page import BasePage
from classWorks.ui_framework2.pages.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.parse_keywords('../datas/market_page.yml', 'goto_search')
        return SearchPage(self.driver)