from urllib.parse import urlparse
from urllib.parse import urlunparse
result = urlparse('https://www.baidu.com/s?wd=python%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F')
print(result)

data = ['https','www.baidu.com','s','','wd=百度','']
url = urlunparse(data)
print(url)
