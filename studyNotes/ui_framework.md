#### 1. 实现UI自动化测试框架，功能包括：关键字，黑名单（装饰器），截图，录屏，日志（配置文件句柄和输出流句柄）
  
#### 作业地址：https://github.com/jumper0419/HogwartsStudy/tree/master/classWorks/ui_framework2

- 关键字：通过解析配置文件来实现功能【yml文件+BasePage.parse_keywords()实现】
- 黑名单：主要是用来异常情况处理
- 截图：异常情况时截图，然后将截图加入到allure中，通过allure来进行展示
- 录屏：用scrcpy工具实现
  - https://github.com/jumper0419/HogwartsStudy/blob/master/classWorks/ui_framework2/conftest.py
- 日志：日志封装+日志初始化+日志的实例化
  - 1）日志封装：https://github.com/jumper0419/HogwartsStudy/blob/master/classWorks/ui_framework2/pages/logger.py
  - 2）日志初始化：BasePage.log()：
    - https://github.com/jumper0419/HogwartsStudy/blob/master/classWorks/ui_framework2/pages/base_page.py
  - 3）日志实例化：https://github.com/jumper0419/HogwartsStudy/blob/master/classWorks/ui_framework2/pages/decorator.py