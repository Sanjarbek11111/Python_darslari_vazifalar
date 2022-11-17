# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:50:43 2022

@author: Python devoloper

"""
class Printer:
    def __init__(self,company,model,maketime):
        self.c=company
        self.m=model
        self.time=maketime
        self.p=0
    def set_probeg(self,probeg):
        ''' Method for to see probeg'''
        self.p =probeg

    def get_info(self):
        ''' Method for get full information'''
        return f'{self.c} \n{self.m} \n{self.time}\n{self.p}'
    def get_company(self):
        ''' This method shows a company of object'''
        return self.c
    def get_model(self):
        ''' This method shows a model of object'''
        return self.m
    def get_mt(self):
        ''' this method shows date of manufacture of object'''
        return self.time
    
printer= Printer('Epson',105,2020)
printer.set_probeg(15000)
#print(printer.get_info())
print(printer.time)
