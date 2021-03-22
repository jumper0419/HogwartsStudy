from mitmproxy import http
class MapLocal2:
  def request(self, flow:http.HTTPFlow):
    if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
      with open('./quote.json', encoding='utf-8') as f:
        flow.response = http.HTTPResponse.make(status_code=200,
                                               content=f.read(),
                                               headers={'Content-Type': 'text/html'}
                                               )
addons = [
  MapLocal2()
]