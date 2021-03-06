from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


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
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    def swipeUp(self):
        """向上滑动"""
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        self.driver.swipe(width*1/2, height*4/5, width*1/2, height*1/5)

    def findElementAndClick(self, locator):
        while True:
            try:
                self.driver.find_element(MobileBy.XPATH, locator).click()
                break
            except:
                print("没有找到元素，需要继续滑动屏幕")
                self.swipeUp()