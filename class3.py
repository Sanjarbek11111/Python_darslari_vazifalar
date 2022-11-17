# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 15:08:36 2022

@author: Python devoloper
"""

class Hospital:
    ''' this class give information about hospitals'''
    def __init__(self,name,location,services,prices,worktime):
        self.name=name
        self.location=location
        self.services=services
        self.prices=prices
        self.worktime=worktime
    def get_info(self):
        return f'{ self.name}\n{self.location}\n{self.service}\n{self.prices}\n{self.worktime}'
    def get_name(self):
        return self.name
    def get_location(self):
        return self.location
    def get_services(self):
        return self.services
    def get_prices(self):
        return self.prices
    def get_worktime(self):
        return self.worktime
    def set_services(self,service):
        self.services.append(service)
# =============================================================================
#     def __str__(self):
#         return self.location
# =============================================================================
    def __repr__(self):
        return self.prices
        
worktime={'Monday':'8.00-18.00',
             'Tuesday':'8.00-18.00',
             'Wednesday':'8.00-18.00',
             'Thursday':'8.00-15.00',
             'Friday':'8.00-17.00',
             'Saturday':'8.00-12.00'}
lokatsiya='Toshkent city,Blok-2,14,2'
services=['endokrinolog','stomatolog','xirurg','ekg','uzi','rentgen']
prices={'Konsultatsiya':150000,
        'Service':'from 100.000 to 2 000.000'}
hospital= Hospital('Hoji bobo',lokatsiya,services,prices,worktime)
hospital.set_services('urolog')
print(hospital)
 



