import requests

url = 'http://www.idannywu.com'
proxy = {
        'https':'http://61.135.217.7:80'
        }
web_data = requests.get(url,proxies=proxy,timeout=3)
print(web_data.status_code)
