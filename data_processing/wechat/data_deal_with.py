import json
import os
from collections import Counter
from pyecharts import Bar,Pie,Line


def get_charts(x,y,label,type1):
    if type1 == 1:
        c = Pie("Pie")
    elif type1 == 2:
        c = Bar("Bar")
    elif type1 == 3:
        c = Line("Line")
    c.add(label,x,y,is_more_utils=True)
    c.show_config()
    c.render("name_analysis_line.html")
    os.system("start name_analysis_line.html")


def data_process():
    with open('info.txt', 'r', encoding='UTF-8')as r:
        result = r.readlines()

    province_list = []
    for i in result:
        print(i)
        province = i.split(',')[-2].split(':')[1].replace('\'', '')
        if str(province) is '':
            print('11111111111111')
            # province = '无'
        province_list.append(province)


    # print(province_list)
    results = str(Counter(province_list)).replace('Counter', '')[1:][:-1]
    print(type(results))
    print(results)
    a = {}
    for i in province_list:
        if province_list.count(i) > 1:
            a[i] = province_list.count(i)
    a = sorted(a.items(), key=lambda item: item[1])
    list1 = []
    list2 = []
    for each in a:
        list1.append(each[0])
        list2.append(each[1])
    get_charts(list1, list2, 'label', 3)


if __name__ == '__main__':
    data_process()
