import allure
from selenium.webdriver.common.by import By

# 黑名单(装饰器)
def handle_blacklist(func):
    def wrapper(*args, **kwargs):
        # 掉不起来，报find_decorator() missing 1 required positional argument: 'func'，用self = args[0]解决
        self = args[0]
        black_list = self.get_datas('../datas/black_list.yml')
        logger = self.log("Ui_Framework", "ui_framework")
        try:
            logger.info("find xpath" + args[2])
            return func(*args, **kwargs)
        except:
            # allure展示异常截图
            allure.attach(self.screenshot(), attachment_type=allure.attachment_type.PNG)
            for exe_xpath in black_list:
                logger.debug("find exe_xpath" + exe_xpath)
                element = self.finds(By.XPATH, exe_xpath)
                if len(element) >= 1:
                    element[0].click()
                    return func(*args, **kwargs)
    return wrapper