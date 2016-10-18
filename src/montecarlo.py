# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:14:42 2016

@author: steiner
"""

import random

#Condições iniciais

S = 1000    #sucetíveis
I = 1       #infectado
R = 0       #recuperado

#Número total de indivíduos
N = S+I+R
N = float(N)

t = 0


#Probabilidade de infecção
beta = .08

# probabilidade de o indivíduo se recuperar
gamma = .01


sList = []      # armazena os indivíduos sucetíveis
iList = []      # armazena os indivíduos infectados
rList = []      # #armazena os indivíduos recuperados
newIList = []   # armazena as pessoas que foram novamente

random.seed()

# Faremos um loop até que não reste nenhum infectuoso
while I > 0:
    newI = 0    
    for i in range(S):
        if random.random() < beta*(I/N):
            newI += 1
            
    recoverI = 0
    for i in range(I):
        if random.random() < gamma:
            recoverI += 1
        
    S -= newI
    I += (newI - recoverI)
    R += recoverI
    
    sList.append(S)
    iList.append(I)
    rList.append(R)
    newIList.append(newI)
    
    print('t', t)
    t += 1
    
import pylab as pl
pl.figure()
pl.xlabel('Sucetiveis')
pl.ylabel('Infectados')
pl.plot(iList)
pl.show()