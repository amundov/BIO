# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 08:55:49 2018

@author: amundov
"""

import csv
import time
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
    
    total=0
    p=[]
    for i in range(0,len(rel)):
        rel[i]=(1/rel[i])
        total+=rel[i]
    for i in range(0,len(rel)):
        p.append(rel[i]/total)
    return p

def calcFitnessScaled(pop):
    dist=[]
    total=0
    rel=[]
    for tour in pop:
        dist.append(calcDist(tour))
        total+=calcDist(tour)
    #print(dist)
    for i in range(0,len(dist)):
        fit = dist[i]/total
        rel.append(fit)
    
    total=0
    p=[]
    for i in range(0,len(rel)):
        rel[i]=(1/rel[i])
        total+=rel[i]
    for i in range(0,len(rel)):
        p.append(rel[i]/total)
    #Scaling
    total = 0
    
    minpos = p.index(min(p))
    for i in range(0,len(p)):
        p[i]=p[i]-p[minpos]
        total+=p[i]
    for i in range(0,len(p)):
        p[i]=p[i]/total
    
    return p

def newRel(subpop):
    p = []
    total = 0
    for i in range(0,len(subpop)):
        total+=subpop[i]
    for i in range(0,len(subpop)):
        p.append(subpop[i]/total)
    return p
        

def matingGround(pop,percent_mating):
    div = 100/percent_mating
    reproduction_size = int((len(pop))/div)
    if reproduction_size%2 == 1:
        reproduction_size+=1
    rand = []    
    for i in range(0,reproduction_size):
        rand.append(random.random()) 
    p = calcFitness(pop) 
    #print(p)
    lucky_ones = []
    mutating_ones = []

    for num in rand:
        dummy = 0
        for i in range(0,len(p)):
            dummy+=p[i]
            if dummy>num:
                lucky_ones.append(i)
                
                break 
    
    #print(lucky_ones)
    return lucky_ones

#40% best reproduces, rest gets mutated. hard. 
def livetsSkole(pop,percent_mating):
    div = 100/percent_mating
    reproduction_size = int((len(pop))/div)
    if reproduction_size%2 == 1:
        reproduction_size+=1
    rand = []    
    for i in range(0,reproduction_size):
        rand.append(random.random()) 
    p = calcFitness(pop)
    
    master = [(i,p[i]) for i in range(len(p))]
    
    #print(p)
    lucky_ones = []
    mutating_ones = []

    for num in rand:
        dummy = 0
        for i in range(0,len(p)):
            dummy+=p[i]
            if dummy>num:
                lucky_ones.append(i)
                
                break 
    
    #print(lucky_ones)
    return lucky_ones


def makeChildren(lucky_ones,pop):
    children = []
    for i in range(0,len(lucky_ones),2):
        a,b = twoPMX(pop[lucky_ones[i]],pop[lucky_ones[i+1]])
        children.append(a)
        children.append(b)
        
    return children

def selection(pop,children):
    newPop= pop+children
    
    rank = calcFitness(newPop)
    
    for i in range(0,len(children)):
        minpos = rank.index(min(rank))
        del(rank[minpos],newPop[minpos])
        
    return newPop

def mutationTiny(subpop):
    
    for tour in subpop:
        a = tour.pop(random.randint(0,len(tour)-1))
        tour.insert(random.randint(0,len(tour)-1),a)
        print(a)
     
    
    return subpop

def mutationLarge(subpop):
    for tour in subpop:
        shuffle(tour)
    return subpop

    

def main(pop_size,turnover,t):
    
    pop = createPopulation(pop_size)
    time_start=time.time()
    #while time.time()-time_start < t:
    for i in range(0,50):
        avg_dist = 0
        selected = matingGround(pop,turnover)
        children = makeChildren(selected,pop)
        pop =selection(pop,children)
        for tour in pop:
            avg_dist+=calcDist(tour)
        #print(pop[0])
    dist = []
    for tour in pop:
            dist.append(calcDist(tour))
    
    
    return dist

def average(pop,num):
    total = 0
    
    for i in range(0,num):
        dist = main(pop,20,0)
        for d in dist:
            total+=d
        
    return( total/(pop*num))
    
        
        
    
        


















