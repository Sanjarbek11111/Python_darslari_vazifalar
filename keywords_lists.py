# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 02:32:03 2022

@author: ACER
"""

def talaba_soni(ism,familiya,**informations):
    informations['ism']=ism
    informations['familiya']=familiya
    return informations
talaba=talaba_soni('Tohir','Ergashev',yil=2000,yoshi=2022,kurs=3)
talaba2=talaba_soni('otash','Rajabov',yil=2001,yoshi=2022,kurs=4)
print(talaba)
print(talaba2)
