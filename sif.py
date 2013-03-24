# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:25:57 2012

@author: Guy
"""
import networkx as nx
import autoviv

def nx_unweighted_read(filename):
    __g = nx.Graph()
    sif_file = file(filename, 'r')
    for line in sif_file:
        line = line.strip("\n")
        ls = line.split("\t")
        __g.add_edge(ls[0],ls[2])
    return __g
    
def nx_unweighted_write(g,filename):
    sif_out = file(filename, 'w')
    for e in g.edges():
        string = '%s\t1.0\t%s\n' % (e[0],e[1])
        sif_out.write(string)

def edges_unweighted_write(a,filename):
    sif_out = file(filename, 'w')
    for e in a:
        string = '%s\t1.0\t%s\n' % (e[0],e[1])
        sif_out.write(string)
        
def edges_unweighted_read(filename):
    sif_in = file(filename, 'r')
    __g = autoviv.refstruct()
    for line in sif_in:
        line = line.strip("\n")
        ls = line.split("\t")
        __g[ls[0]][ls[2]] = 1
    return __g
        
    