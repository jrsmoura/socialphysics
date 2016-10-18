# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:20:33 2016

@author: steiner
"""

import numpy as np
from scipy.optimize import fsolve

def func(x):
    return x - 1. + np.exp(-( 1. + (l/alpha)*p )*x)


n = 1000
alpha = 0.5
l = 1.0
pp = np.linspace(0.00001, 1., num=n)
r = np.zeros(n)
i = 0

print pp


for p in pp:
    r[i] = fsolve(func, 2000)
    i = i + 1
#print r

import matplotlib.pyplot  as pyplot

a = pyplot.subplot()
a.set_xscale('log')
#a.set_yscale('log')
pyplot.plot(pp,r)

pyplot.xlabel('p')
pyplot.ylabel('r$_\infty$')
pyplot.show()
