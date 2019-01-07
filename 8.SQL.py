# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:08:25 2018

@author: Siewling 
for Data Quest Guided Project #7: Analyzing CIA Factbook Data Using SQLite and Python
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("factbook2.db")
q= "SELECT * FROM sqlite_master WHERE type='table';"
data = pd.read_sql_query(q,conn)
q1 = "SELECT * FROM facts "
fulldata = pd.read_sql_query(q1,conn)
print(pd.read_sql_query(q1,conn).head(5))
print(pd.read_sql_query(q1,conn).columns)

q2 = "SELECT Min(population),Max(population),Min(population_growth),Max(population_growth) FROM facts"
reading = pd.read_sql_query(q2,conn)

q3 = "SELECT name FROM facts WHERE population =0"
country0people= pd.read_sql_query(q3,conn)
q4 = "SELECT name FROM facts WHERE population =7256490011"
countryMaxpeople= pd.read_sql_query(q4,conn)

q5 = "SELECT population,population_growth,birth_rate,death_rate from facts WHERE population !=0 AND population !=7256490011"
hisdata = pd.read_sql_query(q5,conn)
# create histogram
fig = plt.figure(figsize=(12,12))
p1 = fig.add_subplot(2,2,1)
p2 = fig.add_subplot(2,2,2)
p3 = fig.add_subplot(2,2,3)
p4 = fig.add_subplot(2,2,4)
p1.hist(hisdata["population"],20,range=(0,513949445))
p2.hist(hisdata["population_growth"],20,range=(0,5))
p3.hist(hisdata["birth_rate"],20,range=(0,50))
p4.hist(hisdata["death_rate"],20,range=(0,15))
p1.set_title("population")
p2.set_title("population_growth")
p3.set_title("birth_rate")
p4.set_title("death_rate")
plt.show()