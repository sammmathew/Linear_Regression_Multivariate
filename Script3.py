# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scipy as sp;
import numpy as np;
import os
import matplotlib as mp

#Clearing the console
os.system('cls');
os.system('clear');

num = raw_input("Enter how many elements you want: ")
p0= raw_input('Define probablity for zero: ')
if float(p0)>=0 and float(p0)<=1:
    num_array=np.random.choice(2,int(num),p=[float(p0),float(1-float(p0))] );
    li=list(num_array);
    p0=(float(li.count(0))/float(len(li)));
    p1=(float(li.count(1))/float(len(li)));
    xm=[0.1,0.3,0.5,0.7,0.8];  #p(X=0/m)
    m=[0.01,0.04,0.03,0.02,0.9]; # p(m)
    
    px_den=sum(np.array(m)*(np.array(xm)))
    print "\n"
   
    ######Binomail approach##############3
    
    No=int(round(int(num)*p0 ))
    Pm=[]
    num=int(num)
    
    Pm=np.power((xm),No)*np.power(1.0-np.array(xm),(num-No));
    Pvec=(Pm*(m))/(sum(Pm*(m)))
    l=list(num_array)
    l1=l.count(1)
    l0=l.count(0)
    pr=float(float(l1)/float(num_array.size))
    pr0=float(float(l0)/float(num_array.size))
    print 'The probability P(m|vector) using Binomial distribution'
    print Pvec
    print"\n"   
    print 'The probability P(X=0|vector) using Binomial approach is : '+str(pr0)
    print "\n"
    
    
    ###########Binomial approach##############3
    
    for i in range(1,int(num)):
        if(num_array[i]==0):
            #print (((np.array(m)*(np.array(xm)))/sum(np.array(m)*(np.array(xm)))));
            px=((np.array(m)*(np.array(xm)))/px_den)
            m=px
            px_den=sum(np.array(m)*(np.array(xm)))
            Pxv=sum(xm*px)
            #Please uncomment below scripts to see the how probability change in Bayesian approach by an entry of xero
            #print 'The probability P(m|vector) affected by "zero" at position: ' +str(i+1)+' of vector'
            #print px
            #print "\n"
        else:
            px=px;
    print 'The probability P(m|x1,x2,x3...xn) affected by "zeros" of vector'
    print px
    print "\n"
    print 'The probability P(X=0|vector)'            
    print Pxv
    print "\n"  
       
else:
    print 'Probaility cannot be greater than 1. Please enter a value between 0 and 1'
