import numpy as np;
import scipy as sp;
x=np.random.choice(2,4000, p=[0.2,0.8])
l = list(x)
l1=l.count(1)
l0=l.count(0)
pr=float(float(l1)/float(x.size))
pr0=float(float(l0)/float(x.size))
print 'Probability of zero is: '+str(pr0)
print 'Probability of one is: ' + str(pr)

####Estimates calculation
ex=0;
for i in range(0,4000):
    if (x[i]==1):
        ex=ex+(x[i]);
    else:
        ex=ex;
        
Ex=float(ex)/4000;
print 'Expected value of an entry of vector is :' +str(Ex);
print 'Expected value of the elements in vector is :'+ str(ex)
        