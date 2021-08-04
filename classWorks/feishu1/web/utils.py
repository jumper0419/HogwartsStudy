import logging
import logging.handlers
import os

import allure
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Utils:
  def yaml_load(self, file_path, data_key=""):
    """
    yaml文件流转成json数据对象
    :param file_path:
    :param data_key:
    :return:
    """
    datas = []
    if file_path != "":
      with open(file_path, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
      if data_key == "":
        return datas
      else:
        return datas[data_key]
    return datas

  def log_init(self, log_id, log_name):
    """
    规范输出日志的格式
    :param log_id: log内容中的标识
    :param log_name: 生成日志的名字
    :return:
    """
    # 第一步：创建一个logger
    logger = logging.getLogger(log_id)
    logger.setLevel(logging.DEBUG)
    # 保证log_id一致的情况下，只创建一次
    if not logger.handlers:
      # 第二步加入句柄
      ## 1）设置日志格式
      log_format_str = '[%(asctime)s]  %(filename)s:%(lineno)d:%(funcName)s: %(message)s'
      format = logging.Formatter(log_format_str)
      ## 2）生成句柄：文件句柄和输出流句柄
      ### 2.1) 日志名
      log_path = os.path.dirname(os.getcwd()) + '\\logs\\'
      log_final_name = log_path + log_name + '.log'
      ### 2.2）生成文件句柄
      h = logging.handlers.RotatingFileHandler(log_final_name, mode='a', encoding="utf-8")
      h.setFormatter(format)
      ### 2.3）生成输出流句柄
      s = logging.StreamHandler()
      s.setFormatter(format)
      # 第三步： 加入句柄
      logger.addHandler(h)
      logger.addHandler(s)
    # print(f"logger.handles: {logger.handlers}")
    return logger

  # def handle_blacklist(self, driver:WebDriver, func):
  #   def wrapper(*args, **kwargs):
  #     black_list = self.yaml_load("datas/black_list.yaml")
  #     logger = self.log_init("FeiShu_BlackList_Handle", "blacklist_handle")
  #     try:
  #       logger.info("find xpath" + args[2])
  #       return func(*args, **kwargs)
  #     except:
  #       # allure展示异常截图
  #       allure.attach(self.screenshot(), attachment_type=allure.attachment_type.PNG)
  #       for exp_xpath in black_list:
  #         logger.debug("find exp_xpath" + exp_xpath)
  #         element = driver.find_elements(By.XPATH, exp_xpath)
  #         if len(element) >= 1:
  #           element[0].click()
  #           return func(*args, **kwargs)
  #
  #     return wrapper