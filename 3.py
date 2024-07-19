# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:04:56 2024

@author: 3student139
"""

import numpy as np

def create_vac():
    row = int(input("Enter number of rows: "))
    
    arr5 = []
    
    for i in range(row):
        rows = []
        value = int(input(f"Enter value at ({i}): "))
        rows.append(value)
        arr5.append(rows)

    arr5 = np.array(arr5)
    return arr5

us = create_vac()
print("Array created:")
print(us)

    