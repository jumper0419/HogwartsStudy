"""
# 关于app的相关操作
1) 启动、重启、停止
"""
import yaml
from appium import webdriver

from classWorks.po_app_tencent.pages.base_page import BasePage
from classWorks.po_app_tencent.pages.main_page import MainPage


with open('../datas/caps.yml') as f:
    datas = yaml.safe_load(f)
    caps = datas['caps']
    host = datas['server']['host']
    port = datas['server']['port']

class App():
    def start(self):
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote(f"http://{host}:{port}/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main(self):
        return MainPage(self.driver)

