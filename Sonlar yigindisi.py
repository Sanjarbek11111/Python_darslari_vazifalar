# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 03:57:43 2022

@author: Python devoloper Python asoslari
"""

# Masala. 1 dan n gacha bolgan sonlar yigindisini toping
x=0
n= int(input('Biror son kiriting:'))
s=[]
while True:
    x+=1
    s.append(x)
    if x==n:
        break
    for c in s:
        print(sum(c))
        

    
        
