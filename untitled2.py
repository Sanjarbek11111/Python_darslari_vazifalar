# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 19:56:33 2022

Istalgan sonni kopaytmasini topuvchi dastur
"""

def hisobla(*sonlar):
    yigindi = 1
    for son in sonlar:
        yigindi *= son
    return yigindi
print(hisobla(5,6,4,8,))