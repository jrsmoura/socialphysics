# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:17:36 2016

@author: steiner

Solução numérica do sistema de equações do artigo do bruno
propagação de um rumor

"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy, scipy.integrate

# Parâmetros
l = 0.75
alpha = .01
k = 4.
p = 0.5

# condicoes iniciais
i0 = 0.80
ro0 = 0.10
r0 = 0.00

Y0 = [ i0, ro0, r0 ]

tMax = 5

# vetor tempo ==> para a solução numérica
T = scipy.linspace(0, tMax, 1001)


#Esta função define as equações do modelo a serem integradas

def rhs(Y, t, l, alpha, k):
    '''
    Modelo de propagação de rumores: Gonçlves, et al.

    Aqui temos o lado direto das EDO's.
    '''

    i = Y[0]
    ro = Y[1]
    r = Y[2]

    N = i + ro + r

    # EDO's -- lados direitos
    di = - l*p*k*ro*i - (1. - p)*l*k*ro*i
    dro = l*p*k*ro*i / N - alpha*k*ro*(ro + r)
    dr = alpha*k*ro*(ro + r) + (1. - p)*l*k*ro*i

    # vetor de saida contendo todas as solucoes
    dY = [ di, dro, dr ]

    return dY

# Integracao das EOD's
# CUIDADO: O integrador das equações sobrescreve os valores inciais
#  'args' -- passa os parâmetros para o lado direto das equações
#            várias vezes
solution = scipy.integrate.odeint(rhs,
                                  Y0,
                                  T,
                                  args = (l, alpha, k))

i = solution[:, 0]
ro = solution[:, 1]
r = solution[:, 2]

N = i + ro + r


# Construção do gráfico

import pylab

pylab.figure()

pylab.plot(T, i,
           T, ro,
           T, r)

pylab.xlabel('Tempo')
pylab.ylabel('Proporcao')

pylab.legend([ 'Ignorante', 'Propagadores', 'Sriflers' ])

pylab.show()
