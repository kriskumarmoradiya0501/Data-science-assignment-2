# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:33:45 2024

@author: 3student139
"""

import numpy as np


m1 = np.array([[125,65],[1,2]])
m3 = np.linalg.inv(m1)

print("Matrix 1 : ",m1)
print("Inverse : ",m3)
   # np.linalg.inv(mtrix)