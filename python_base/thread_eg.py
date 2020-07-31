# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           thread_eg.py
   Description:
   Author:        
   Create Date:    2020/07/31
-------------------------------------------------
   Modify:
                   2020/07/31:
-------------------------------------------------
"""
# Description: python 多线程-普通多线程-生产者消费者模型

import re
import time
import requests
import threading
from lxml import etree
from bs4 import BeautifulSoup
from queue import Queue
from threading import Thread


def producer(in_q):  # 生产者
    ready_list = []
    while in_q.full() is False:
        for i in range(1, 77):
            url = 'https://www.baidu.com/s?wd=python&pn='+str(i*10)
            if url not in ready_list:
                ready_list.append(url)
                in_q.put(url)
            else:
                continue


def consumer(in_q, out_q):  # 消费者
    headers = {
        'Connection': 'keep-alive',
        'Cookie': 'BIDUPSID=EF529B3CB84F0EB47BE015AC14619281; PSTM=1587951206; BD_UPN=12314753; BAIDUID=DB5DA6CCBAD9B804CF9BEA53D2D3DC9F:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-340%3A; BDUSS=DVER2FtUU9GQjgtM2sxMktNQWUzb3l0aXZKUHV0VkxpNjdCLWdUNktWUjJ0RWhmSVFBQUFBJCQAAAAAAAAAAAEAAAB-vqpjztLP687Ssru5u7rDYW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHYnIV92JyFfV; BDUSS_BFESS=DVER2FtUU9GQjgtM2sxMktNQWUzb3l0aXZKUHV0VkxpNjdCLWdUNktWUjJ0RWhmSVFBQUFBJCQAAAAAAAAAAAEAAAB-vqpjztLP687Ssru5u7rDYW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHYnIV92JyFfV; delPer=0; BD_CK_SAM=1; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=2; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_PSSID=32293_1435_31670_31253_32348_32046_32395_32405_32429_32116_31708_26350_32437_31640; H_PS_645EC=13ec8nHjh%2BtzdguB4H2AKFzh6FuHqCF2lJm70D9YdTju1DjKMj5KoKgQ4K0J6fLwscHd; BDSVRTM=169; COOKIE_SESSION=1_0_3_3_1_1_0_0_3_1_1_0_1596164956_0_0_0_1596174022_0_1596175858%7C9%230_0_1596164935%7C1',
        'DNT': '1',
        'Host': 'www.baidu.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    while True:
        url = in_q.get()
        resp = requests.get(url, headers=headers)
        html = etree.HTML(resp.text)
        url_list = html.xpath('//div[@class="result c-container "]/h3/a/@href')

        out_q.put(str(threading.current_thread().getName()) + ' - ' + str(url) + ' - ' + str(url_list))
        in_q.task_done()  # 通知生产者，队列已消化完


if __name__ == '__main__':
    start = time.time()
    queue = Queue(maxsize=10)  # 设置队列最大空间为10
    result_queue = Queue()
    print('queue 开始大小 %d' % queue.qsize())

    producer_thread = Thread(target=producer, args=(queue,))
    producer_thread.daemon = True
    producer_thread.start()

    for index in range(10):
        consumer_thread = Thread(target=consumer, args=(queue, result_queue, ))
        consumer_thread.daemon = True
        consumer_thread.start()

    queue.join()
    end = time.time()
    print('总耗时：%s' % (end - start))
    print('queue 结束大小 %d' % queue.qsize())
    print('result_queue 结束大小 %d' % result_queue.qsize())

    for i in range(1, 78):
        print(result_queue.get())
        if result_queue.empty():
            break


