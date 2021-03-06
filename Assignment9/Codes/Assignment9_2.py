# -*- coding: utf-8 -*-
"""Assignment9_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rtQFtegPcshwwOdlz-xReIxJFGDGqEM3
"""

#Code by K.A. Raja Babu
#June 14, 2021

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#Points
A = np.array([0,0,0]).reshape((3,1))
B = np.array([0,0,15]).reshape((3,1))
C = np.array([8.449,0,15]).reshape((3,1))
D = np.array([11.38,0,16]).reshape((3,1))
E = np.array([22.76,0,0]).reshape((3,1))
V = np.array([2,0,5]).reshape((3,1))

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)

#Generating and plotting v_b
x_AV = line_gen(A,V)
plt.plot(x_AV[0,:],x_AV[1,:],x_AV[2,:])
plt.quiver(2,0,5,2.3,0,5)

#Generating and plotting v_p
plt.quiver(0,0,15,4,0,0)

#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:])
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:])

#Generating and Plotting path of bullet
yp=np.linspace(0,0,23)
x = np.linspace(0,22.76,23)
p=np.poly1d([-0.124,2.823,0])
for i in range(len(x)):
    y=p(x)
plt.plot(x,yp,y,'--',label='Path of Bullet')

#drawing angle arc
r=6
theta = np.linspace(1.230,1.570,50)
x1 = r*np.cos(theta)
y1 = r*np.sin(theta)
ya = np.linspace(0,0,50)
plt.plot(x1,ya,y1)

#plotting point
ax.scatter(A[0],A[1],A[2],'o',label='Bullet Starting Pt.')
ax.scatter(B[0],B[1],B[2],'o',label='Plane Starting Pt.')
ax.scatter(C[0],C[1],C[2],'o',label='Hitting Pt.')
ax.scatter(D[0],D[1],D[2],'o',label='Max. Height')
ax.scatter(E[0],E[1],E[2],'o')

#Labelling points
ax.text(-0.4,-0.012,0.3, "A")
ax.text(-0.4,-0.012,15.3, "B")
ax.text(7.60,0.002,15.5, "C")
ax.text(11.0,0.005,16.3, "D")
ax.text(0.2,0.0001,6.5,'$ \u03B8 $')
ax.text(2.5,0.001,4,'$v_b$')
ax.text(2.5,0.01,15,'$v_p$')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()

plt.show()