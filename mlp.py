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
   
    def earlystopping(self, inputs, targets, valid, validtargets,iterations):
        e = self.fullError(valid,validtargets)
        
        while True:
            self.train(inputs,targets,iterations)
            dummy = self.fullError(valid,validtargets)
            print(dummy)
            if dummy<e:
                e = dummy
            else: 
                break
    
    def fullError(self,inputs,targets):
        E = 0
        for i in range(len(inputs)):
            z,y = self.forward(inputs[i])
            E += self.error(y,targets[i])
        return E
                              
    def error(self,y,target):
        e = 0
        for i in range(len(y)):
            e+=((y[i]-target[i])**2)
        return 0.5*e


    def train(self, inputs, targets,iterations):
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
    
    def evaluate(self,test, targets):
        right = 0
        wrong = 0
        
        for i in range(len(test)):
            z,y = self.forward(test[i])
            print(y,targets[i])
            if y.index(max(y)) == list(targets[i]).index(max(list(targets[i]))):
                right+=1
            else:
                wrong+=1
        return right,wrong, right/(right+wrong)
            


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
        conf = np.zeros((np.shape(self.w)[1],np.shape(self.w)[1]))
        for i in range(len(inputs)):
            z,y = self.forward(inputs[i])
            target = list(targets[i])
            
            index = target.index(max(target))
            prediction = y.index(max(y))
            conf[prediction][index]+=1
        
        print(conf)