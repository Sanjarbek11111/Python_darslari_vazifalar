# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 02:53:28 2022

@author: ACER
"""

def talaba_soni(ism,familiya,**informations):
    informations['ism']=ism
    informations['familiya']=familiya
    return informations
talaba=talaba_soni('Tohir','Ergashev',kurs=3,yoshi=22,t_yil=2022-22)
talaba2=talaba_soni('otash','Rajabov',kurs=4)
print(talaba)
print(talaba2)