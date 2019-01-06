# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:34:21 2019

@author: Siew Ling
for Data Quest Guided Project #1: Explore U.S. Births
"""

def read_csv(name):
    f=open(name,'r')
    string_list=f.read().split('\n')
    f.close()
    data_header = string_list[0:1]
    print(data_header)
    #last row is empty, first row is header
    string_list = string_list[1:len(string_list)-1]
    final_list= []
    for each in string_list:
        each = each.replace("\"","")
        string_fields = each.split(',')
        int_fields = []
        for i in string_fields:
            int_field = int(i)
            int_fields.append(int_field)
        final_list.append(int_fields)
    return final_list
    
def month_births(lol):
    births_per_month = {}
    for row in lol:
        month = row[1]
        births = row[4]
        if month in births_per_month:
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    return births_per_month

def dow_births(lol):
    births_per_dow = {1:0,2:0,3:0,4:0,5:0,6:0,7:0}
    for row in lol:
        day = row[3]
        births = row[4]
        if day in births_per_dow:
            births_per_dow[day] += births
        else:
            births_per_dow[day] = births
    return births_per_dow

def calc_counts(data,column):
    births_per_column = {}
    for row in data:
        key = row[column]
        births = row[4]
        if key in births_per_column:
            births_per_column[key] += births
        else:
            births_per_column[key] = births   
    return births_per_column
    
    

cdc_list = read_csv('US_births_1994-2003_CDC_NCHS.csv')
cdc_month_births = month_births(cdc_list)
print(cdc_month_births)
cdc_day_births = dow_births(cdc_list)
print(cdc_day_births)
cdc_year_births = calc_counts(cdc_list,0)
cdc_month_births = calc_counts(cdc_list,1)
cdc_dom_births = calc_counts(cdc_list,2)
cdc_dow_births = calc_counts(cdc_list,3)

"""
Write a function that can calculate the min and max values for any dictionary that's passed in.
Write a function that extracts the same values across years and calculates the differences between consecutive values to show if number of births is increasing or decreasing.
For example, how did the number of births on Saturday change each year between 1994 and 2003?
Find a way to combine the CDC data with the SSA data, which you can find here. Specifically, brainstorm ways to deal with the overlapping time periods in the datasets.
"""





