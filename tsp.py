# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:46:09 2018

@author: amundov
"""

import numpy as np
import pandas as pd
import math
from sympy import isprime
import time
from random import shuffle

cities_ = pd.read_csv('cities.csv')
cities_['prime'] = cities_['CityId'].apply(isprime)

#Using dict datatype in stead of dafaframe to reduce runtime
cities = cities_.sample(20).to_dict()


path=list(range(len(cities['X'])))
shuffle(path)

def dist(x1,y1,x2,y2,st_num,x_is_prime):
    cf = 1.1 if (st_num % 10 == 0 and not x_is_prime ) else 1
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)*cf



def cost(path,cities):
    cost = 0
    is_prime = False
    
    for i,city_id in enumerate(path):
        step = i+1
        #x_is_prime = cities['prime'][city_id]
        print(i,city_id)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        