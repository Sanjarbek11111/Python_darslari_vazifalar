# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 11:23:15 2022

@author: ACER
"""

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


print(fibonacci(1))
