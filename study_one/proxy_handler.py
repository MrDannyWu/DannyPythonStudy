from urllib.error import URLError
from urllib.request import ProxyHandler
from urllib.request import build_opener

proxy_handler = ProxyHandler({
    'http':'http://221.202.72.250:53281'
    })
opener = build_opener(proxy_handler)
try:
    res = opener.open('https://www.baidu.com')
    print(res.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
