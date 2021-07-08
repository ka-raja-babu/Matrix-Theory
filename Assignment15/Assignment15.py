# -*- coding: utf-8 -*-
"""Assignment15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w02aX1wFmrqmKbW3dzveoJvBnGCQtWUY
"""

#Code by K.A. Raja Babu
#July 08,2021

import numpy as np
import matplotlib.pyplot as plt
import math

#Defining f(x)
def f(x,a,b,d):
	return a*(x**2)+b*x+d
a = -1/2
b = 4
d = 0

#For maxima using gradient ascent
cur_x = -2
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1 
max_iters = 100000000 
iters = 0

#For minima 
x1=-2
x2=4
x3=4.5
mn=min(f(x1,a,b,d),f(x2,a,b,d),f(x3,a,b,d))

#Defining derivative of f(x)
df = lambda x: 2*a*x + b           

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

print("Maximum value of f(x) is ",f(cur_x,a,b,d), "at","x =",cur_x)
print("Minimum value of f(x) is ",mn, "at","x =",np.roots([a,b,-mn])[1])

# plotting f(x)
x=np.linspace(-3,11,40)
y=-0.5*(x**2)+4*x
plt.plot(x,y,label='$4x-0.5x^2$')
plt.plot(cur_x,f(cur_x,a,b,d),'o')
plt.text(cur_x*(1+0.1), f(cur_x,a,b,d)*(1+0.02),'P(4,8)')
plt.plot(-2,-10,'o')
plt.text(-1.8,-11,'Q(-2,-10)')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid()
plt.legend()
plt.show()