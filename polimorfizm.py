# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 01:28:29 2022

@author: Python devoloper
"""


from class3 import Hospital
class Shifoxona(Hospital):
    def __init__(self,name,location,prices,services,worktime,features,workers):
        self.name=name
        self.location=location
        self.services=services
        self.prices=prices
        self.worktime=worktime
        self.features=features
        self.workers=workers
        super().__init__(name,location,prices,worktime)
    def __str__(self):
        return self.location

        
    
worktime={'Monday':'8.00-18.00',
             'Tuesday':'8.00-18.00',
             'Wednesday':'8.00-18.00', 
             'Thursday':'8.00-15.00',
             'Friday':'8.00-17.00',
             'Saturday':'8.00-12.00'}
lokatsiya='Toshkent city,Blok-2,14,2'
services=['endokrinolog','stomatolog','xirirg','ekg','uzi','rentgen']
prices={'Konsultatsiya':150000,
        'Service':'from 100.000 to 2 000.000'}
hospital= Shifoxona('Hoji bobo',lokatsiya,prices,services,worktime,'uzi','Dr.Haydarov')
print(Shifoxona)