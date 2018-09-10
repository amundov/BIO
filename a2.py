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



def pmx(parent1,parent2):
    start = random.randint(0,8)
    stop= random.randint(start,8)
    child = [0]*9
    
    
    #Lager kopi av segment i child
    for i in range(start,stop+1):
        child.insert(i,parent1[i])
        del(child[len(child)-1])
    
    #Finner indexer i s2 som inneholder elementer i child
    index = []
    for i in range(0,len(s2)):
        if i not in range(start,stop+1):
            if s2[i]in child:
                index.append(i)
    #Finner overkopierte verdier i S2 som  ikke er i child           
    value= []
    for i in range(start,stop+1):
        if s2[i] not in child:
            value.append(s2[i])
    #tilordner overkopierte verdier i s2 nye indexer.
    if len(value)==len(index):
        for i in range(0,len(value)):
            child.insert(index[i],value[i])
            del(child[index[i]+1])
    #kopierer det som gjenstår
    for i in range(0,len(child)):
        if child[i]==0:
            child.insert(i,s2[i])
            del(child[i+1])
             
    return child

def twochildrenPMX(parent1,parent2):
    child1=pmx(parent1,parent2)
    child2=pmx(parent1,parent2)
    return child1,child2
 
s3 = [1,2,3,4,5,6,7,8,9]
s4 = [9,3,7,8,2,6,5,1,4]   
def ordercrossover(parent1,parent2):
    start = random.randint(0,8)
    stop= random.randint(start,8)
    #start,stop = 3,6
    child = [0]*9
    #Lager kopi av segment i child
    for i in range(start,stop+1):
        child.insert(i,parent1[i])
        del(child[len(child)-1])
    #lager liste over verider som skal plasseres i child
    value = []
    for i in range(stop+1,len(child)):
        if parent2[i] not in child:
            value.append(parent2[i])
    for i in range(0,stop+1):
        if parent2[i] not in child:
            value.append(parent2[i])
            
    for i in range(stop+1,len(s2)):
        child.insert(i,value.pop(0))
        del(child[i+1])
    for i in range(0,start):
        child.insert(i,value.pop(0))
        del(child[i+1])   
            
    return child

def twochildrenOrder(parent1,parent2):
    child1=ordercrossover(parent1,parent2)
    child2 = ordercrossover(parent1,parent2)
    return child1,child2

    

def cycle(parent1,parent2):
    length = len(parent1)
    index = []
    k = 0
    values = []
    child = [0]*9
    teller = 0
    start = parent1[k]
    
    
    
    while len(values)!=len(child):
        for i in range(0,len(parent1)):
            if i not in index:
                k = i
                break
        while teller<len(parent1):
            if parent1[k] in values:
                break
            else:
                values.append(parent1[k])
                index.append(k)
                teller+=1
    
                for i in range(0,len(parent1)):
                    if parent2[i]==parent1[k]:             
                        k = i
                        print(k)
                        break
                    
        for i in range(0,len(parent1)):
            if i not in index:
                k = i
                break
                
        while teller<len(parent2):
            if parent2[k] in values:
                break
            else:
                values.append(parent2[k])
                index.append(k)
                teller+=1
    
                for i in range(0,len(parent2)):
                    if parent1[i]==parent2[k]:             
                        k = i
                        print(k)
                        break
    for i in range(0,9):
        child.insert(index[i],values[i])
        del(child[index[i]+1])
        
        
                   
        
         
    return child    
            
def maketwocycles(parent1,parent2):
    return cycle(parent1,parent2),cycle(parent2,parent1)
           
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    