from classWorks.ui_framework2.pages.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        return self.parse_keywords('../datas/search_page.yml', 'search')