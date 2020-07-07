import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
def get_web_source():
    with open('pylib_data.html','r') as r:
        data = r.read()
    return data

#print(data)
def get_url_list(web_source):
    #url = 'https://www.lfd.uci.edu/~gohlke/pythonlibs/'
    base_url = 'https://download.lfd.uci.edu/pythonlibs/h2ufg7oq/'
    #try:
    #    web_source = requests.get(url).text
    #except:
    #    print('请求失败！')
    soup = BeautifulSoup(web_source,'lxml')
    names = soup.select('.pylibs li ul li a')
    url_list = []
    str1 = names[0].text
    #str2 = str1.encode('utf-8').decode('windows-1252')
    #str2.encode('windows-1252').decode('utf-8')
    print(str1)

    print(str1)
    for name in names:
        #name1 = str(name.text)
        #name1.replace(' ','_')
        #print(name1)
        url = base_url+name.text
        #print(url)
        if '.whl' in url:
            print(url)
            url_list.append(url)
            with open('E:\\Desktop\\url.txt','a',encoding='utf-8') as f:
                f.write(url+'\n')
    return url_list
#web_source = get_web_source()
#url_list = get_url_list(web_source)
#print(url_list)
def download_whl(url):
    try:
        source = requests.get(url)
    except:
        print('请求资源错误！')
    file_name = url.split('/')[-1]
    print('正在下载：'+file_name)
    with open('E:\\Desktop\\python_whl\\'+file_name,'wb') as f:
        f.write(source.content)
#download_whl('https://download.lfd.uci.edu/pythonlibs/h2ufg7oq/ad3_2.2.1_cp27_cp27m_win32.whl')
def main():
    pool = Pool(20)
    web_source = get_web_source()
    url_list = get_url_list(web_source)
    #print(url_list)
    pool.map(download_whl,url_list)
    pool.close()
if __name__ == '__main__':
    main()

