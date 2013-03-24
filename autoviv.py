# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:41:48 2013

@author: guy
"""

class refstruct(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

def pretty(dictionary, indent=0):
    for key, value in dictionary.iteritems():
        print '\t' * indent + str(key)
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print '\t' * (indent+1) + str(value)
            
def stringify(L,sep,*length):
    
    # Length is for if you want to repeat a single value    
    l = 1
    if length:
        l = length[0]
    string = ''
    if L is list:
        for i in range(len(L)):
            if i == 0:
                string = '%s' % L[i]
            else:
                string = '%s%s%s' % (string,sep,L[i])
    else:
        for i in range(0,l):
            if i == 0:
                string = '%s' % L
            else:
                string = '%s%s%s' % (string,sep,L)
    return string

def other_ones(L,one):
    
    # Returns other members of a list besides the one
    
    assert type(L) is list, 'Must be a list'
    
    others = list()
    
    for m in L:
        if m == one:
            pass
        else:
            others.append(m)
    
    if others > 1:
        return others
    else:
        return others[0]