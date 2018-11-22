# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 13:45:01 2018

@author: amundov
"""

def testSpeed(df,dict_):
    start1 = time.time()
    s1 = 0
    for i in range(len(df)):
        s1+=df['X'][i]
    end1 = time.time()
    start2 = time.time()
    s2 = 0
    for i in range(len(dict_['X'])):
        s2+=dict_['X'][i]
    end2 = time.time()
    start3 = time.time()
    array_ = list(df['X'].values)
    s3 = 0
    for i in range(len(array_)):
        s3+=array_ [i]
    end3 = time.time()
    
    
    return(s1,s2,end1-start1,end2-start2,(end1-start1)/(end2-start2), s3,end3-start3)
        