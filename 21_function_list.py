# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:20:59 2022

@author: ACER
"""
ismlar=['knnncc','rfererrf','erffff','erervvv','revvevf','veeefws']

def royxat(x):
    nomlar=[]
    harf=ismlar[:]
    while harf:
        
        ism=harf.pop()
        nomlar.append(ism.title())
    return nomlar
harflar=royxat(ismlar)
print(harflar)
print(ismlar)