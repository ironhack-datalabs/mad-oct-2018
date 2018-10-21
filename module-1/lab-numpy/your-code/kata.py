# Data Analytics Bootcamp October 2018 - IronHack
# Ivan Cernicharo Ortiz October 21, 2018
# Welcome to my kata solutions for the challenges proposed 
# for numpy module lab for Data Analytics Bootcamp at IronHack


##################################################################
## First KATA: weird matrix multiplication
## I had a serious issue with this one. Even having passed 
## the tests, when I try to attemp it returns me a Timeout error
## message. I have tried many ways but without success.
## Need your feedback in this one
import numpy as np
def weird_mul(A, B):
    sa=np.shape(A)
    sb=np.shape(B)
    if (sa!=(0,0) and len(sa)<=2) and (sb!=(0,0) and len(sb)<=2):
        for i in range(len(A)):
            for k in range(len(B)):
                if k==0:
                    d=np.hstack(np.outer(A[i],B[k]))
                else:
                    d=np.vstack((d,np.hstack(np.outer(A[i],B[k]))))
            if i==0:
                e=d
            else:
                e=np.vstack((e,d))
        return e
    else:
        return None


##################################################################
## Second KATA: Insert Dashes
## No problems found with this one
def insert_dash(num):
    numm=str(num)
    nm=""
    if len(numm)>1:
        for i in range(len(numm)-1):
            if int(numm[i])%2!=0 and int(numm[i+1])%2!=0:
                nm=nm+numm[i]+"-"
            else:
                nm=nm+numm[i]
            if i==len(numm)-2:
                nm=nm+numm[i+1]
    else:
        nm=numm
    return nm


##################################################################
## Third KATA: Thinkful - Logic Drills: Red and Bumpy
## No problems found with this one

def color_probability(color, texture):
    if texture=='bumpy':
        num=7.0
        if color=='red':
            prob=4/num
        elif color=='yellow':
            prob=2/num
        else: # Color: green
            prob=1/num
    else: # Smooth texture
        num=3.0
        prob=1/num
    return str(prob)[:4]

# Feedback will be greatfull
# Thank you for your time