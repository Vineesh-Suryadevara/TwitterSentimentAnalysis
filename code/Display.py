# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:29:14 2019

@author: Vineesh's PC
"""
import matplotlib.pyplot as mp
import pandas as pd
File = pd.read_csv(input('Enter the file name:'))
result = pd.DataFrame(File)

result = result.drop(['id'], axis = 1)
sample_result = result[:10000]
mp.hist(sample_result)
