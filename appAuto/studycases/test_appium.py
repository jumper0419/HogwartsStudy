from appium import webdriver

# 初始化参数
desire_cap = {
    "platformName": "android",
    "platformVersion": "11.0",
    "deviceName": "emulator-5554",
    # "app": "F:\\api_autoTest_tools\\android_studio\\SDK\\packages\\xueqiuv6.0_yxdown.com.apk",
    # "appPackage": "com.tencent.wework",  # app包名
    # "appActivity": ".msg.controller.MessageListActivity",  # 启动launch Activity
    # "appActivity": ".setting.controller.SettingLanguageListActivity",
    "appPackage": "com.android.chrome",
    "appActivity": "com.google.android.apps.chrome.Main",
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)