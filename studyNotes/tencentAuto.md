## 微信小程序自动化
#### 一、adb proxy 工具使用
- https://ceshiren.com/t/topic/3994
- 命令：
  mitmdump -p 5038 \
  --rawtcp --mode reverse:http://localhost:5037  \
  -s tcp.py
  
- adb proxy 起了个代理，是为了修复chromedriver相关bug
- 5037是chromedriver使用的端口
- 5038是我们反向代理tcp的一个端口，监听的5037
    