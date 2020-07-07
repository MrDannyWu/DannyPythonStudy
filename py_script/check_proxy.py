import requests
# 开始判断哪些ip是可以用的
def check_one_proxy(proxy):
    url = 'http://www.idannywu.com'
    if 'https' in proxy:
        proxy_dict = {
            'https':proxy
        }
    else:
        proxy_dict = {
            'http':proxy
        }
        print(proxy)


    response = requests.get(url,proxies = proxy_dict,timeout=5)
    print(response.status_code)
    #访问状态
    if response.status_code == 200:
        print('这个代理ip可用'+proxy)
        return proxy
    else:
        print('不可用')
        return proxy


with open('proxy1.txt','r+') as r:
    proxys = r.readlines()
    proxy_list = []
    for proxy in proxys:
        proxy = proxy.replace('\n','')
        proxy_list.append(proxy)
        check_one_proxy(proxy)
        #print(proxy)
    #print(proxy_list)

'''
file_object = open('proxy.txt','rU')
try:
    for line in file_object:
        print(do_something_with(line))
except:
    pass
finally:
    file_object.close()
'''
