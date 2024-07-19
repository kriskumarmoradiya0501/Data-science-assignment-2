# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:23:07 2024

@author: 3student139
"""

import numpy as a

ar = a.array([[1],
              [2],
              [3],
              [4],
              [5]])

ar1 = ar.reshape(1,-1)

print(ar1)