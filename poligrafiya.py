# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 18:52:30 2022

@author: Python devoloper
"""

class Poligrafiya:
    def __init__(self, name):
        self.name= name
        self.books=[]
    def __repr__(self):
        return self.name
    def __add__(self,y):
        return self.name+ poli2.name
    def add_book(self,*book):
        for a in book:
            return self.books.append(book)
    def __len__(self):
        return len(self.books)
        
# =============================================================================
#     def __call__(self):
#         return self.books
# =============================================================================
    def get_info(self):
        return self.books 
        
class Books:
    def __init__(self,name, author,date_made,pages):
        self.name= name
        self.author= author
        self.date_made= date_made
        self.pages= pages
    def get_info(self):
        info= f'{self.name}, {self.author},{self.date_made},{self.pages}'
        return info
poli1= Poligrafiya('Muallim Print\n')
poli2= Poligrafiya('Iftixor print')
poli3= poli1+  poli2


book1= Books('Tarixi Muhammadiy','Alixon To\'ra Sog\'uniy','1918-yil',346)
book2= Books('Headway Beginner','John and Liz Soars',2014,144)
book3= Books('Headway Elementary',' John and Liz Soars',2015,160)
book4= Books('Solutions','Otabek Rajobov',2015,162)
book5= Books('O\'tgan Kunlar','Abdulla Qodiriy',1936,312)
#print(book1.get_info())
poli1.add_book(book1,book2)
poli2.add_book(book3,book4,book5)
print(len(poli1) )

