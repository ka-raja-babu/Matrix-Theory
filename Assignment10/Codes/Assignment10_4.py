# -*- coding: utf-8 -*-
"""Assignment10_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zOXrhoG91cz41oVLiE_PEf9MnepStpY6
"""

#Decrease in Sales from Sep to Oct(in Rupees)
#Code by K.A. Raja Babu
#June 14 ,2021
import numpy as np
import matplotlib.pyplot as plt
  
N = 2
ind = np.arange(N) 
width = 0.25
  
xvals = [5000,30000]
bar1 = plt.bar(ind, xvals, width, color = 'r')
  
yvals = [10000,20000]
bar2 = plt.bar(ind+width, yvals, width, color='g')
  
zvals = [24000,0]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')
  
plt.xlabel("Farmers")
plt.ylabel('Sales(in Rupees)')
plt.title("Decrese in Sales from Sep to Oct(in Rupees)")
  
plt.xticks(ind+width,['Ramkishan', 'Gurucharan Singh'])
plt.legend( (bar1, bar2, bar3), ('Basmati', 'Permal', 'Naura') )
plt.show()