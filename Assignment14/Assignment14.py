# -*- coding: utf-8 -*-
"""Assignment14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_aHaRl-HMGWRpozCm5YhEOHs3KudJ8y3
"""

#Probability Distribution of X
#Code by K.A. Raja Babu
#July 04 ,2021

import numpy as np
import matplotlib.pyplot as plt

# creating the dataset
data = {'$X_i$=0':1/2, '$X_i$=1':1/2}
X = list(data.keys())
prob = list(data.values())
  
fig = plt.figure()
 
# creating the bar plot
plt.bar(X,prob,width = 0.3)
 
plt.xlabel("$X_i$")
plt.ylabel("Pr($X_i$)")
plt.title("Probability Distribution of $X_{i=0,1,2}$")

plt.show()