# -*- coding: utf-8 -*-
"""Assignment5_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19YYMrsphetaval6f6rn3FagQfkaaq4tb
"""

#Code by K.A. Raja Babu
#May 24, 2021
import numpy as np
import matplotlib.pyplot as plt
from coeffs import * #referred from G.V.V sir's Code

#centre and radius of circles
O=np.array([-2,0])
r=5

#point on circle
A=np.array([O[0]+r,O[1]])


#Generating line
x_OA = line_gen(O,A)

#Plotting line
plt.plot(x_OA[0,:],x_OA[1,:],label='$r=5$')

#Plotting circle
c1 = 5
theta1 = np.linspace(0,2*np.pi,50)
x1 = c1*np.cos(theta1)
y1 = c1*np.sin(theta1)

plt.plot(x1-2,y1,label='$circle$')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(2,3,'o')
plt.text(1.9,3.2,'A')
plt.plot(-2,0,'o')
plt.text(-2.2,0.2,'O')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')
plt.show()