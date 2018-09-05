# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:45:37 2018

@author: amundov
"""

""" Representations; 
    Binary
        Mutations and crossovers
    Interger
        Crossover, random resetting and creep
    Real-Valued or floating point
    
    Permutation
    partially mapped crossover,
    Tree
    
"""

"""Crossover"""
import random
s1 = [2,4,7,1,3,6,8,9,5]
s2 = [5,9,8,6,2,4,1,3,7]


start,stop = 3,7
def pmx(parent1,parent2):
    #start = random.randint(0,8)
    #stop= random.randint(start,8)
    child = [0]*9
    for i in range(start,stop+1):
        child.insert(i,parent1[i])
        del(child[len(child)-1])
    temp = []
    
    for i in range(start,stop+1):
        for j in range(start,stop+1):
            if child[i]==parent2[j]:
                temp.append(parent2[j])
    
            
           
    return child,temp


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    