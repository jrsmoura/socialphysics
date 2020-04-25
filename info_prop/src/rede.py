# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:34:35 2016

@author: steiner
"""



#The package which handles the graph objects
import networkx as nx

# Matplotlib is the default package for
# rendering the graphs
import matplotlib.pyplot as plt

def simple_graph():

    #create an empty graph
    G = nx.Graph()
    
    #add three edges
    G.add_edge('A','B');
    G.add_edge('B','C');
    G.add_edge('C','A');

    #draw the graph
    nx.draw(G)

    #show
    plt.show()

simple_graph()

