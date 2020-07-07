import requests
from lxml import etree
import multiprocessing
import time
def get_all_proxy(queue):
#def get_all_proxy():
    url = 'http://www.xicidaili.com/nn/1'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    response = requests.get(url,headers=headers)
    # with open('xici.html','wb') as f:
    #     f.write(response.content)
    # 只需要ip及端口号，提取
    html_ele = etree.HTML(response.text)
    ip_ele = html_ele.xpath('//table[@id="ip_list"]/tr/td[2]/text()')  #要看打印在html中的文件，因为有的网页中有而没打印出来，以自己打印的为主
    port_ele = html_ele.xpath('//table[@id="ip_list"]/tr/td[3]/text()')
    http_type = html_ele.xpath('//table[@id="ip_list"]/tr/td[6]/text()')
    # print(len(ip_ele))
    # print(len(port_ele))
 
    proxy_list = []
    for i in range(0,len(ip_ele)):
        #proxy_list.append(proxy_str)
        #print(proxy_str)
        #print(http_type[i])
        if http_type[i] in 'HTTP':
            proxy_str = 'http://'+ip_ele[i]+ ':' +port_ele[i]
            queue.put(proxy_str)  #将拼接的ip及端口，放到进程中
            #print(proxy_str)
        else:
            proxy_str = 'https://'+ip_ele[i]+ ':' +port_ele[i]
            queue.put(proxy_str)  #将拼接的ip及端口，放到进程中
            #print(proxy_str)
    # return proxy_list
#get_all_proxy()

# 开始判断哪些ip是可以用的
def check_one_proxy(proxy):
    try:
        url = 'http://www.idannywu.com'
        if 'https' in proxy:
            proxy_dict = {
                'https':proxy
            }
        else:
            proxy_dict = {
                'http':proxy
            }

        try:
            response = requests.get(url,proxies = proxy_dict,timeout=5)
            #访问状态
            if response.status_code == 200:
                print('这个代理ip可用'+proxy)
                return proxy
            else:
                print('不可用'+proxy)
                return proxy
        except:
            print('不可用的代理'+proxy)
    except Exception as e:
        print(e)
 
 
if __name__ == "__main__":
    # 创建消息对列
    q = multiprocessing.Queue()
    # 如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()
    # 创建进程 ，获取所有的代理ip
    p = multiprocessing.Process(target=get_all_proxy,args=(q,))
    p.start()
    # 检验代理可用性
    pool = multiprocessing.Pool(50)
    result_list = []
    while True:
        try:
            proxy_str = q.get(timeout =5)
        except:
            break
        proxy_re = pool.apply_async(check_one_proxy,(proxy_str,))
        #print(proxy_re)  获取的是进行进程池的对象<multiprocessing.pool.ApplyResult object at 0x0000000003CAF400>
        result_list.append(proxy_re)
    valid_proxy_list = []
    for proxy_re in result_list:
        result = proxy_re.get()
        # print(result)  #获取到每个ip加端口号 或者none
        if result is None:
            pass
        else:
            valid_proxy_list.append(result)
 
    print('可用的代理有：')
    print(valid_proxy_list)
    for i in valid_proxy_list:
        with open('proxy1.txt','a+') as f:
            f.write(i+"\n")
    pool.close()
    pool.join()
    p.join()
