# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 07:18:57 2019

@author: Siew Ling
for Data Quest Guided Project #2: Exploring Gun Deaths in the US
"""

import csv
import datetime

f=open('guns.csv')
fcsv=csv.reader(f)
data=list(fcsv)
f.close()
print(data[0:5],"\n")

headers = data[0:1]
data = data[1:]
print(headers)
print(data[0:5])

years = [ int(each[1]) for each in data]
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
print(year_counts)

dates =[datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
print(dates[0:5])

date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
print(date_counts)

sex_counts = {}
for each in data:
    if each[5] in sex_counts:
        sex_counts[each[5]] += 1
    else: 
        sex_counts[each[5]] = 1
race_counts = {}
for each in data:
    if each[7] in race_counts:
        race_counts[each[7]] += 1
    else: 
        race_counts[each[7]] = 1
print(sex_counts)
print(race_counts)

f = open('census.csv')
fcsv = csv.reader(f)
census = list(fcsv)
print(census)

mapping ={"Asian/Pacific Islander":15159516 + 674625, 
          "Black": 40250635, 
          "Native American/Native Alaskan": 3739506, 
          "Hispanic": 44618105,
          "White": 197318956
        }
race_per_hundredk = {}
for each in race_counts:
    race_per_hundredk[each] =race_counts[each]/mapping[each]*100000
print(race_per_hundredk)

intents = [each[3] for each in data]
races = [each[7] for each in data]
homicide_race_counts = {}
for i,race in enumerate(races):
    if intents[i]=='Homicide':
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1
for each in homicide_race_counts:
    homicide_race_counts[each] = homicide_race_counts[each]/mapping[each]*100000
print(homicide_race_counts)
# it appears that gun related homicide in the US is disproportionately affecting Black and Hispanic people.
"""
Here are some potential next steps:

Figure out the link, if any, between month and homicide rate.
Explore the homicide rate by gender.
Explore the rates of other intents, like Accidental, by gender and race.
Find out if gun death rates correlate to location and education.
"""
        
