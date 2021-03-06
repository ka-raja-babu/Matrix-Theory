# -*- coding: utf-8 -*-
"""ChallengeProblem3_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1app0wxrbBoJ1MbL_L1S22a4zzsSN741I
"""

#Code by K.A. Raja Babu 
#June 21,2021
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 100)

y = 21*x**2 -28*x + 10 

plt.plot(x,y,label='y=21$x^2$-28x+10')
plt.grid()

plt.plot(2/3,2/3, 'o')
plt.text(0.62,1.2,'c')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend()
plt.ylim([0,20])
plt.show()