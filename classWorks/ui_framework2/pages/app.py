from appium import webdriver

from classWorks.ui_framework2.pages.base_page import BasePage
from classWorks.ui_framework2.pages.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver == None:
            caps = self.get_datas('../datas/apps.yml', 'caps')
            server = self.get_datas('../datas/apps.yml', 'server')
            host = server['host']
            port = server['port']
            self.driver = webdriver.Remote(f"http://{host}:{port}/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main(self):
        return MainPage(self.driver)