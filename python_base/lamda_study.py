# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           lamda_study.py
   Description:    lamda学习
   Author:        
   Create Date:    2020/07/30
-------------------------------------------------
   Modify:
                   2020/07/30:
-------------------------------------------------
"""


add = lambda x, y :\
    x + y
print(add(1, 1))

sq = lambda x : x * x

res = map(sq, [i for i in range(100)])
print(res)
for j in res:
    print(j)

class Lamb(object):

    res = lambda self, x: x


la = Lamb()
print(la.res(1))