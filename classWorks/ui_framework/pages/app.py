import yaml
from appium import webdriver

from classWorks.ui_framework.pages.base_page import BasePage
from classWorks.ui_framework.pages.main_page import MainPage

with open('../datas/apps.yml') as f:
    datas = yaml.safe_load(f)
caps = datas["caps"]
host = datas["server"]["host"]
port = datas["server"]["port"]
print(host, port)

class App(BasePage):

    def start(self):
        if self.driver == None:
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

    # def a(self):
    #     return a