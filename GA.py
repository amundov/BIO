# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 08:55:49 2018

@author: amundov
"""

import csv
from itertools import permutations
from random import shuffle,randint

with open("european_cities.csv","r") as file:
    data = list(csv.reader(file,delimiter=';'))


cities = []

for i in range(1,len(data)):
    dummy=[]
    for j in range(0,len(data)-1):
        dummy.append(data[i][j])
    cities.append(dummy)


def calcDist(tour):
    dist = 0
    for i in range(0,len(tour)-1):
        dist +=float(cities[tour[i]][tour[i+1]])
    return dist

def createPopulation(size):
    pop = []
    for i in range(0,size):
        tour=list(range(0,len(data)-1))
        shuffle(tour)
        pop.append(tour)   
    return pop

def calcFitness(pop):
    dist=[]
    total=0
    rel=[]
    for tour in pop:
        dist.append(calcDist(tour))
        total+=calcDist(tour)
    for i in range(0,len(dist)):
        fit = dist[i]/total
        rel.append(fit)
    rel.sort()
    total=0
    p=[]
    for i in range(0,len(rel)):
        rel[i]=(1/rel[i])
        total+=rel[i]
    for i in range(0,len(rel)):
        p.append(rel[i]/total)
        

        #print(dist)
    return dist ,rel,p


























