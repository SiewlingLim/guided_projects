# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 07:05:00 2018

@author: Siewling
for Data Quest Guided Project #4: Visualizing Earnings Based On College Majors
"""

import pandas as pd
from pandas import scatter_matrix
recent_grads = pd.read_csv("recent-grads.csv")
"""
print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())
print(recent_grads.describe())
"""
#rank 1-173, with 21 columns
#19 columns are numbers
print(recent_grads.info())
raw_data_count = len(recent_grads)
recent_grads = recent_grads.dropna()
cleaned_data_count = len(recent_grads)
"""
recent_grads.plot(x='Sample_size', y='Median', kind='scatter', title='Median vs. Sample_size', figsize=(5,5))
#larger sample size has wider range median, overall sample size is less than 1000
recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter', title='Unemployment_rate vs. Sample_size', figsize=(5,5))
#average umployment 0.007 aross sample size
recent_grads.plot(x='Full_time', y='Median', kind='scatter', title='Median vs. Full_time', figsize=(5,5))
recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter', title='Unemployment_rate vs. ShareWomen', figsize=(5,5))
recent_grads.plot(x='Men', y='Median', kind='scatter', title='Median vs. Men', figsize=(5,5))
recent_grads.plot(x='Women', y='Median', kind='scatter', title='Median vs. Women', figsize=(5,5))
"""
#recent_grads.plot(x='Rank', y='Median', kind='scatter', title='Median vs. Rank', figsize=(5,5))
##definitely, higher rank, higher median pay
#recent_grads.plot(x='ShareWomen', y='Median', kind='scatter', title='Median vs. ShareWomen', figsize=(5,5))
##major with more woman has lower median pay
#recent_grads.plot(x='Full_time', y='Median', kind='scatter', title='Median vs. Full_time', figsize=(5,5))
##no correlation between number of full time and the median pay

"""
print(recent_grads["ShareWomen"].value_counts().sort_index())
recent_grads["Sample_size"].hist(bins=100,range=(0,5000))
recent_grads["Employed"].hist(bins=100,range=(0,310000))
"""
#recent_grads["ShareWomen"].hist(bins=2,range=(0,1))
##more than 50% of the major has more woman graduates
#recent_grads["Median"].hist(bins=20,range=(0,100000))
##most common median is 30,000 t0 40,000

scatter_matrix(recent_grads[['Sample_size','Median']],figsize=(10,10))
#scatter_matrix(recent_grads[['Sample_size','Median','Unemployment_rate']],figsize=(10,10))

recent_grads.head(10).plot.bar(x='Major', y='ShareWomen')
recent_grads.tail(10).plot.bar(x='Major', y='ShareWomen')
recent_grads.head(10).plot.bar(x='Major', y='Unemployment_rate')
recent_grads.tail(10).plot.bar(x='Major', y='Unemployment_rate')