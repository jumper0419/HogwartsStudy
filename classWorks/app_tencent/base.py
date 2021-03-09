from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class Base:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["skipDeviceInitialization"] = "true"
        caps["dontStopAppOnReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def swipeUp(self):
        """向上滑动"""
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        self.driver.swipe(width*1/2, height*4/5, width*1/2, height*1/5)

    def findElementAndClick(self, locator, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"翻页{num}次，没有找到元素")
            self.driver.implicitly_wait(1)
            try:
                self.driver.find_element(MobileBy.XPATH, locator).click()
                self.driver.implicitly_wait(5)
                break
            except:
                print("没有找到元素，需要继续滑动屏幕")
                self.swipeUp()