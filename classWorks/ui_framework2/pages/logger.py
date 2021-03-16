# 定义 log 的基础内容
import logging
import logging.handlers
import os

def log_init(log_id, log_name):
    # 第一步：创建一个logger
    logger = logging.getLogger(log_id)
    logger.setLevel(logging.DEBUG)
    #保证log_id一致的情况下，只创建一次
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