"""

"""
import numpy as np
import random
class mlp:
    def __init__(self, inputs, targets, nhidden):
        self.beta = 1
        self.eta = 0.02
        self.momentum = 0.0
        self.v = np.random.random(((len(inputs[0])+1),nhidden))
        self.w = np.random.random((nhidden+1,len(targets[0])))
        
        #making the weigths "small enough"
        self.v = (self.v-0.5)/20
        self.w = (self.w-0.5)/20
        print(self.w)
       
    
    
    """def initializeWeights(self,v,w):
        
        for i in range(np.shape(v)[0]):
            for j in range(np.shape(v)[1]):
                v[i][j] = random.uniform(-0.3,0.3)
        
        for i in range(np.shape(w)[0]):
            for j in range(np.shape(w)[1]):
                w[i][j] = random.uniform(-0.3,0.3)"""
        
    
    
    def earlystopping(self, inputs, targets, valid, validtargets):
        print('To be implemented')

    def train(self, inputs, targets,iterations = 100):
        index = list(range(len(inputs)))
        random.shuffle(index)
        k = 0
        for i in range(iterations):
            print(k)
            for i in range(len(inputs)):
                z,y = self.forward(inputs[index[i]])
                self.backward(y,targets[index[i]],z,inputs[index[i]])
            k+=1
        return self.w

    def forward(self, inputs):
        #Calulation of values in hidden layer
        z = [0]*(np.shape(self.v))[1]
        for i in range(len(z)):
            z[i]+=self.v[0][i]
            for k in range(1,np.shape(self.v)[0]):
                z[i]+= (self.v[k][i]*inputs[k-1])
        #Calculation of output
        y = [0]*(np.shape(self.w))[1]
        for i in range(len(y)):
            y[i]+=self.w[0][i]
            for k in range(1,np.shape(self.w)[0]):
                y[i]+=(self.w[k][i]*z[k-1])
        
        return z,y
    
    def backward(self,output,target,z,inputs):
        #deltas of output layer:
        d0 = []
        for i in range(0,len(output)):
            d0.append(output[i]-target[i])
        #deltas of hidden layer: 
        dh = np.zeros(np.shape(z))
        for j in range(1,np.shape(self.w)[0]):
            for i in range(np.shape(self.w)[1]):
                dh[j-1] += d0[i]*self.w[j][i]

        #updating w
        for i in range(np.shape(self.w)[1]):
            self.w[0][i] -= (self.eta*d0[i])
        
        for i in range(1,np.shape(self.w)[0]):
            for k in range(np.shape(self.w)[1]):
                self.w[i][k] -= (self.eta*z[i-1]*d0[k])
                
        
        for i in range(np.shape(self.v)[1]):
            self.v[0][i] -= (self.eta*dh[i])
            
        for i in range(1,np.shape(self.v)[0]):
            for k in range(np.shape(self.v)[1]):
                self.v[i][k] -= (self.eta*inputs[i-1]*dh[k])
        #no return, self.v and self.w are updated. 
    
                

    def confusion(self, inputs, targets):
        print('To be implemented')
