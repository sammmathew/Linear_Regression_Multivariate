# -*- coding: utf-8 -*-
"""
Created on Fri Feb 01 18:26:50 2019

@author: Sam
"""
import scipy as sc;
import numpy as np;
import os
import matplotlib as mp
os.system('cls')
# Input training and test data
train= np.loadtxt("F:\UTA\EE5359_ML\Assignment2\Submission\Training.txt", dtype='f', delimiter=',');
test=np.loadtxt("F:\UTA\EE5359_ML\Assignment2\Submission\Test.txt", dtype='f', delimiter=',')
#Input polynomial order and regularization factors
order=(raw_input("Enter the max polynomial order needed: "))
lamda_in = raw_input("Enter the regularization factors in a line seperated by space (Do not press Enter key till all factors are input):" ).split()
o=np.array(range(1,int(order)+1))

lamda = []
for i in lamda_in:
    lamda.append(int(i))
print sum(lamda) # Regularization parameters in array
color=iter(mp.pyplot.cm.rainbow(np.linspace(0,1,np.size(lamda))))
mp.pyplot.close('all')

#For each regularization parameter (lamda) plot training and testing error for each polynomial degree
for val in lamda:
    print "\n"+"####################################################"
    print "REGULARIZATION FACTOR "+str(val);
    if (val!=0):
        mp.pyplot.figure(val)
        tr_err=[];
        ts_err=[];
        y_tst=[];
        for val2 in o:
            
            #print "\n"
            #print 'Reg term is: '+str(val)+' polynomial term is: '+ str(val2)
            [w,train_err]=lin_regr(train,val2,val); # User define Linear regression function for training
            #print 'RSS for train data with polynomial order '+str(val2)+' and reg term '+ str(val)+ ' is: '+ str(train_err)
            if train_err!= 'NA':
                tr_err=np.append(tr_err,train_err);
                [test_err,y_tst]=lin_regr_test(test,val2,val, w)# User define Linear regression function for testing
                ts_err=np.append(ts_err, test_err)
             #   print 'RSS for test data with polynomial order '+str(val2)+' and reg term '+str(val)+ ' is: '+ str(test_err)
        #Figure plot
        
        mp.pyplot.title('Polynomial order vs RSS plot for regularization factor: ' +str(val))
        mp.pyplot.grid()
        mp.pyplot.xlabel('Polynomial degree')
        mp.pyplot.ylabel('RSS')
        mp.pyplot.plot(o,tr_err,'-b', label='Train error')
        mp.pyplot.plot(o,ts_err,'-r', label='Test error')
        mp.pyplot.legend();
        
        mp.pyplot.figure(100)
        c=next(color)
        mp.pyplot.title('Estimated test output vs Real test output')
        
        mp.pyplot.xlabel('n')
        mp.pyplot.ylabel('f(x) or y')
        
        mp.pyplot.plot(range(0,int(test[:,7:8].shape[0])),y_tst, c=c, label='Estimated for lamda'+str(val));
        #mp.pyplot.plot(range(0,int(test[:,7:8].shape[0])),test[:,7:8], 'k-.', label='Real output');
        mp.pyplot.legend();
         
# Condition for regularization parameter (lamda=0) treated seperately to avoid Inputs with deficient matrix
    else:
        y_tst=[];
        for val2 in o:
            print "\n"
            print 'Reg term is: '+str(val)+'and  polynomial term is: '+ str(val2)
            [w,train_err]=lin_regr(train,val2,val);
            print 'RSS for train data with polynomial order '+str(val2)+' and reg term '+ str(val)+ ' is: '+ str(train_err)
            if train_err!= 'NA':
                print tr_err
                tr_err=np.append(tr_err,train_err);
                [test_err, y_tst]=lin_regr_test(test,val2,val, w)
                print 'RSS for test data with polynomial order '+str(val2)+' and reg term '+str(val)+ ' is: '+ str(test_err)
        
mp.pyplot.plot(range(0,int(test[:,7:8].shape[0])),test[:,7:8], 'k-.', label='Test output y');
mp.pyplot.grid()
mp.pyplot.legend();  
#################### User defined function for Linear Regression testing #############

def lin_regr_test(test, o, lamda, w):
    import numpy as np;
    import matplotlib as mp
    x_test=np.transpose(test[:,0:7]);
    y_test=np.transpose(test[:,7:8].flatten())
    p,N=x_test.shape; #p is dimensionality 7
    xapp=np.ones(N) #N number of data=3
    x_test=np.vstack((xapp,x_test))
    #print x_test
    B=np.random.rand((p*(int(o)+1)))
    for j in range(2,int(o)+1):
            #print x.shape
            x_test=np.vstack((x_test,np.power(x_test[1:p+1,:],j)));
    
    y_est_test=np.matmul(w,x_test);
   #print "Yest_test"
    #print y_est_test
    
    #print "Y_test"
    #print y_test
    Error_test=sum(np.power(y_test-y_est_test,2))
   #print 'RSS for test data with polynomial order '+str(o)+' and reg term '+str(lamda)+ ' is: '+ str(Error_test)
    
    return(Error_test,y_est_test)



################# User defined function for Linear REgression training ################

def lin_regr(input, o, lamda):
    #o- Order of polynomial
    #lamda- Regularization term
    
    import numpy as np;
    import matplotlib as mp
    x=np.transpose(input[:,0:7]);
    y=input[:,7:8].flatten();
    #print x.shape
    #print x
    print "ok"
    o=int(o)
    print o
    lamda=int(lamda)
    p,N=x.shape; #p is dimensionality 
    xapp=np.ones(N) #N number of data
    x=np.vstack((xapp,x))
    B=np.random.rand((p*(o)+1))
    for j in range(1,o+1):
        
        x=np.vstack((x,np.power(x[1:p+1,:],j)));
    
    
    l1,l2=x.shape
    fx=np.matmul(B,x)
    RSS=np.sum(np.matmul(np.transpose(y-fx),(y-fx))); # First calculation of RSS
    Bx=[]
    if ((np.linalg.matrix_rank(np.matmul(x,np.transpose(x)))!= int(l1)) and lamda !=0):
            B_int=np.matmul(x,y)
            print  B_int.shape;
            B_int2=np.matmul(x,np.transpose(x))+((np.identity((p*o)+1))*lamda)    
            Bx=np.matmul(np.linalg.inv(B_int2),B_int)
            #Bx=np.matmul(np.matmul(np.linalg.inv((np.matmul(x,np.transpose(x)))+((np.identity((p*o)+1))*lamda)),x),y)
            #print x
            Error=np.matmul(y-np.matmul(Bx,x),np.transpose(y-np.matmul(Bx,x)))#+(lamda*(np.matmul(np.transpose(Bx),Bx)))
            #print "Bx.x"
            #print np.matmul(Bx,x)
            
            #print "Y_Train"
            
            #print y
            #print Error
            
    elif ((np.linalg.matrix_rank(np.matmul(x,np.transpose(x)))== l1)):
            B_int=np.matmul(x,y)
            B_int2=np.matmul(x,np.transpose(x))+((np.identity((p*o)+1))*lamda)
            Bx=np.matmul(np.linalg.inv(B_int2),B_int)
            #Bx=np.matmul(np.matmul(np.linalg.inv((np.matmul(x,np.transpose(x)))+((np.identity((p*o)+1))*lamda)),x),y)
            #print x
            Error=np.matmul(y-np.matmul(Bx,x),np.transpose(y-np.matmul(Bx,x)))#+(lamda*(np.matmul(np.transpose(Bx),Bx)))
            print "Bx.x"
            print np.matmul(Bx,x)
            
            #print "Y_Train"
            
            #print y
            #print Error
    else:
            #print 'X is rank deficient matrix... Try a regularization term other than 0'
            Bx=[]
            Error='NA'
            
       
    return (Bx,Error)
    
    