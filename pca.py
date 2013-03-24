#!/usr/bin/python

'''
PCA class, performs pca on a numpy array
Returns scores and loadings, as well as the cumulative sum of variances
'''

import numpy as np
from matplotlib import pyplot as plt
#from __future__ import division
dot = np.dot

class PCA(object):
    
    def __init__(self,A):
        
        self.U, self.D, self.P = np.linalg.svd(A,full_matrices=False)
        assert np.all( self.D[:-1] >= self.D[1:] )
        
        # Calculate the explained variance per PC
        
        self.eigen = self.D**2
        self.sumvariance = np.cumsum(self.eigen)
        self.sumvariance = self.sumvariance/self.sumvariance[-1]

        # Find the scores and loadings

        self.scores = dot(self.U,np.diag(self.D))
        self.loadings = self.P.T

    def PlotScores(self,pc1,pc2):
        
        plt.scatter(self.scores[:,pc1],self.scores[:,pc2])
        labels = np.arange(np.shape(self.scores)[0])
        for x, y, label in zip(self.scores[:,pc1], self.scores[:,pc2], labels):
            plt.annotate(label, xy=(x,y))
        plt.axvline(color='k',linestyle='--')
        plt.axhline(color='k',linestyle='--')
        plt.xlabel('PC {0}'.format(pc1))
        plt.ylabel('PC {0}'.format(pc2))
        plt.title('Score Plot')

        plt.show()

    def PlotLoadings(self,pc1,pc2):
        
        plt.scatter(self.loadings[:,pc1],self.loadings[:,pc2])
        labels = np.arange(np.shape(self.loadings)[0])
        for x, y, label in zip(self.loadings[:,pc1], self.loadings[:,pc2], labels):
            plt.annotate(label, xy=(x,y))
        plt.axvline(color='k',linestyle='--')
        plt.axhline(color='k',linestyle='--')
        plt.xlabel('PC {0}'.format(pc1))
        plt.ylabel('PC {0}'.format(pc2))
        plt.title('Loadings Plot')

        plt.show()

    def PlotVar(self,pc1,pc2):
       
       plt.plot(range(len(self.loadings)+1),np.concatenate([[0],self.sumvariance]),marker='o')
       plt.xlabel('PC Number')
       plt.ylabel('Var Explained')
       plt.title('Variance Explained')

       plt.show()

    def __getitem__(self, item):
        return item

if __name__ == '__main__':
    
    a = np.random.random([100,50])
    prin = PCA(a)
    prin.PlotVar(1,2)
