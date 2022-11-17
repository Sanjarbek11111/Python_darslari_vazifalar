# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 20:25:51 2022

@author: ACER
"""

def ortacha(min,max):
    sonlar=[] 
    sonlar2=[]
    while min<max:
        sonlar.append(min)
        min+=1
        
    for i in sonlar:
        if i%2==1 and i%3!=0 and i%5!=0 and i%7!=0:
            sonlar2.append(i)
    print(sonlar2)
ortacha(2,88)
                    