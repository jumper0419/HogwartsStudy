# -*- coding=utf-8 -*-
import json
from time import sleep

from mitmproxy import http

class rewrite:
  def response(self, flow:http.HTTPFlow):
    # 只改变符合条件url的响应
    if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
      # 拿到响应
      data = json.loads(flow.response.text)
      # 例子一：将股票名称复制10遍
      raw_name = data["data"]["items"][0]["quote"]["name"]
      change_name = raw_name* 10
      data["data"]["items"][0]["quote"]["name"] = change_name
      # 例子二：将股票涨跌幅反转
      raw_percent = data["data"]["items"][0]["quote"]["percent"]
      if raw_percent > 0:
        change_percent = f"-{raw_percent}"
      else:
        change_percent = abs(raw_percent)
      data["data"]["items"][0]["quote"]["percent"] = change_percent
      # 例子三：测试股票涨跌幅的边界值
      test_value = [-10000, -0.5, -0.01, -0, +0, +0.01734, 100, 20000000]
      for index in range(len(test_value)):
        data["data"]["items"][index+1]["quote"]["percent"] = test_value[index]
      flow.response.text = json.dumps(data)

addons = [
  rewrite()
]
