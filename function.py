# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 18:58:34 2022

@author: ACER
"""

#r= int(input('Aylananing radiusini kiriting:'))
def aylana_yuzi(x):
    
    d=x+x
    pi=3.14
    s=pi*(x**2)
    a=pi*d
    aylana={'Aylana radiusi':x,
            'Aylna diametri':d,
            'Aylana yuzi': s,
            'Aylana uzunligi': a}
    print(aylana)
aylana_yuzi(3)