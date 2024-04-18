import random
from matplotlib.pyplot import *
import numpy

def f(x):
    return x**4+2*x**3-12*x**2-2*x+77.37

def recuit_simule(f,a,b):
    random.seed()
    x=random.random()*(b-a)+a
    y=f(x)
    delta_x=0.1
    Temp=numpy.logspace(2,0,100)
    liste_x=[]
    liste_T=[]
    for T in Temp:
        for i in range(1000):
            u=random.random()
            if u<0.5:
                x1=x+delta_x 
            else:
                x1=x-delta_x
            y1=f(x1)
            if y1<y:
                x=x1
                y=y1
            else:
                u=random.random()
                if u<numpy.exp(-(y1-y)/T):
                    x=x1
                    y=y1 
        liste_x.append(x)
        liste_T.append(T)
    return (x,liste_x,liste_T)
    
def encadrement(f,x1,delta_x):
    y1=f(x1)
    direction=1
    x2=x1+direction*delta_x
    y2=f(x2)
    if y2>y1:
        (x,y)=(x1,y1)
        (x1,y1)=(x2,y2)
        (x2,y2)=(x,y)
        direction=-1
    x3=x2+direction*delta_x
    y3=f(x3)
    while y3<y2:
        x3 += direction*delta_x
        y3 = f(x3)
    return (x1,x2,x3)

def recherche_minimum(f,a,b,c,tol):
    fa=f(a)
    fb=f(b)
    fc=f(c)
    while abs(a-c)>tol:
        x=(a+b)/2
        fx=f(x)
        if fx>fb:
            (a,b,c)=(x,b,c)
        else:
            (a,b,c)=(a,x,b)
        fa=f(a)
        fb=f(b)
        fc=f(c)
        x=(b+c)/2
        fx=f(x)
        if fx>fb:
            (a,b,c)=(a,b,x)
        else:
            (a,b,c)=(b,x,c)
        fa=f(a)
        fb=f(b)
        fc=f(c)
    return (a+c)/2
              

a=-5
b=4
(x1,x,T)=recuit_simule(f,a,b)
figure()
plot(T,x,"ko")
grid()
xlabel("T")
ylabel("x")
xscale('log')
(x1,x2,x3)=encadrement(f,x1,0.01)
xmin=recherche_minimum(f,x1,x2,x3,1e-4)

print(xmin)