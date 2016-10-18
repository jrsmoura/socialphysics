#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:17:36 2016

@author: steiner

Solução numérica do modelo SIR com natalidade e morte


"""
import scipy, scipy.integrate

# Parametros
beta = 5
gamma = 1
mu = 1.0 / 50  

# condicoes iniciais
S0 = 0.99
I0 = 0.01
R0 = 0.00

Y0 = [ S0, I0, R0 ]

tMax = 6

# vetor tempo ==> para a solução numérica
T = scipy.linspace(0, tMax, 1001)


#Esta função define as equações do modelo a serem integradas

def rhs(Y, t, beta, gamma, mu):
    '''
    Modelo SIR.
    
    Aqui temos o lado direto das EDO's.
    '''
    
    S = Y[0]
    I = Y[1]
    R = Y[2]
    
    N = S + I + R
    
    # EDO's -- lados direitos
    dS = mu * N - beta * I * S / N - mu * S
    dI = beta * I * S / N - (gamma + mu) * I
    dR = gamma * I - mu * R
    
    # vetor de saida contendo todas as solucoes
    dY = [ dS, dI, dR ]

    return dY

# Integracao das EOD's
# CUIDADO: O integrador das equações sobrescreve os valores inciais
#  'args' -- passa os parâmetros para o lado direto das equações
#            várias vezes
solution = scipy.integrate.odeint(rhs,
                                  Y0,
                                  T,
                                  args = (beta, gamma, mu))
        
S = solution[:, 0]
I = solution[:, 1]
R = solution[:, 2]

N = S + I + R


# Construção do gráfico

import pylab

pylab.figure()

pylab.plot(T, S / N,
           T, I / N,
           T, R / N)

pylab.xlabel('Tempo')
pylab.ylabel('Proporcao')

pylab.legend([ 'Suscetivel', 'Infectado', 'Recuperado' ])

pylab.show()
