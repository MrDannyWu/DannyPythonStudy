# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           wrapper_study.py
   Description:    装饰器学习
   Author:        
   Create Date:    2020/07/30
-------------------------------------------------
   Modify:
                   2020/07/30:
-------------------------------------------------
"""
import time


def time_wrapper(func):
    """
    不含参数的装饰器
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f = func(*args, **kwargs)
        exec_time = time.time() - start_time
        return exec_time, f
    return wrapper

def time_decorator(param):
    """
    含参数的装饰器
    :param param:
    :return:
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            print('%s----%s' % (param, func.__name__))
            f = func(*args, **kwargs)
            exec_time = time.time() - start_time
            return exec_time, f
        return wrapper
    return decorator


@time_decorator('hhh')
def add(a, b):
    sum = 0
    for i in range(1000000):
        sum = a + b + sum
    return sum

# s = time_wrapper(add)
# print(s(1,2))

print(add(1,2344))

class People(object):

    str_text = '我是类属性'

    def __init__(self, name, gender):
        self._name = name
        self.gender = gender

    @property
    def people_name(self):
        return self._name

    @people_name.setter
    def people_name(self, value):
        self._name = value

    @classmethod
    def add(cls, a, b):
        print('类方法：', a + b, cls.str_text)

    @staticmethod
    def sub(a, b):
        print('静态方法：', a - b, People.str_text)





peop = People('Danny', 'Man')
print(peop.people_name)
peop.people_name = 'Hello'
print(peop.people_name)
peop.add(1, 2)
peop.sub(2, 1)
People.add(1, 2)
People.sub(2, 1)