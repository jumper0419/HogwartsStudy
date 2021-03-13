import yaml
from appium.webdriver.common.mobileby import MobileBy

black_list = yaml.safe_load(open("../datas/black.yml", encoding='utf-8'))


def find_decorator(func):
    def run(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            # 掉不起来，报find_decorator() missing 1 required positional argument: 'func'，用self = args[0]解决
            self = args[0]
            for exe_xpath in black_list:
                element = self.finds(MobileBy.XPATH, exe_xpath)
                if len(element) >= 1:
                    element[0].click()
                    self.find_decorator(func)
    return run


def b(func):
    def run(*args, **kwargs):
        print("hello")
        func(*args, **kwargs)
    return run