# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:30:17 2018

@author: amundov
"""

import csv
from itertools import permutations

with open("european_cities.csv","r") as file:
    data = list(csv.reader(file,delimiter=';'))
    

cities6 = []

for i in range(1,5):
    dummy=[]
    for j in range(0,4):
        dummy.append(data[i][j])
    cities6.append(dummy)   
    



def exhaustive(cities):
    dist = 0
    for tour in list(permutations(range(len(cities)))):
        dummy = 0
        for i in range(0,len(tour)-1):
            dummy +=float(cities[tour[i]][tour[i+1]])
            print(dummy)
    
    
    for i in range(0,len(cities)-1):
        dist+=float(cities[i][i+1])
    return tour    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        