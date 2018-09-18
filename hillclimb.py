# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 21:22:15 2018

@author: amundov
"""

import csv
from random import shuffle,sample, randint
import time

with open("european_cities.csv","r") as file:
    data = list(csv.reader(file,delimiter=';'))

del(data[0])

def swapTwoRandom(tour):
    i,j = random.sample(range(len(tour)),2)
    tour[i],tour[j]=tour[j],tour[i]
    return tour

def swapNabo(tour):
    i = random.randint(0,len(tour)-1)
    j = (i+1)%(len(tour))
    #using modulo operator to get index 0 if i at end of tour
    tour[i],tour[j]=tour[j],tour[i]
    return tour
        
def calcDist(tour):
    dist = 0
    for i in range(0,len(tour)-1):
        dist+=float(data[tour[i]][tour[i+1]])
    return dist

def hillBilly(t): 
    time_start = time.time()
    tour = list(range(len(data)))
    shuffle(tour)
    challenger = tour
    
    dist = calcDist(tour)
    n = 0
    while time.time()-time_start < t:
        #checikg 10 random neigbours
        shuffle(challenger)
        n+=1
        for i in range(0,10):
            
            challenger = swapTwoRandom(challenger)
            beta = calcDist(challenger)
            if beta<dist:
                dist = beta
                tour = challenger
                print(dist,tour)
        
        if n>10000:
            temp = tour
            for i in range(0,10):
                challenger = swapNabo(temp)
                beta = calcDist(challenger)
                if beta<dist:
                    dist = beta
                    tour = challenger
                    print(dist,tour, 'alternativ')
            
        
    return dist,n
    

    
        
    



#time_start = time.time()
#short = 1000000
##
  #  shuffle(tour)
    
    

#print(short)   
#for tour in list(permutations(range(len(cities)))):
 #   dummy = 0
  #  for i in range(0,len(tour)-1):
   #     dummy +=float(cities[tour[i]][tour[i+1]])
    #    if dummy<short:
     #       short=dummy