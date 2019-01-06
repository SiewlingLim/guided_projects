# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:13:44 2018

@author: Siew Ling
for Data Quest Guided Project #6: Analyzing NYC High School Data
"""

import pandas as pd
import numpy
import re
import matplotlib.pyplot as plt

#from mpl_toolkits.basemap import Basemap


data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]

data = {}

for f in data_files:
    d = pd.read_csv("schools/{0}".format(f))
    data[f.replace(".csv", "")] = d


# # Read in the surveys
all_survey = pd.read_csv("schools/survey_all.txt", delimiter="\t", encoding='windows-1252')
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter="\t", encoding='windows-1252')
survey = pd.concat([all_survey, d75_survey], axis=0)

survey["DBN"] = survey["dbn"]

survey_fields = [
    "DBN", 
    "rr_s", 
    "rr_t", 
    "rr_p", 
    "N_s", 
    "N_t", 
    "N_p", 
    "saf_p_11", 
    "com_p_11", 
    "eng_p_11", 
    "aca_p_11", 
    "saf_t_11", 
    "com_t_11", 
    "eng_t_11", 
    "aca_t_11", 
    "saf_s_11", 
    "com_s_11", 
    "eng_s_11", 
    "aca_s_11", 
    "saf_tot_11", 
    "com_tot_11", 
    "eng_tot_11", 
    "aca_tot_11",
]
survey = survey.loc[:,survey_fields]
data["survey"] = survey

# # Add DBN columns
data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

def pad_csd(num):
    string_representation = str(num)
    if len(string_representation) > 1:
        return string_representation
    else:
        return "0" + string_representation
    
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]


# # Convert columns to numeric
cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']
for c in cols:
    data["sat_results"][c] = pd.to_numeric(data["sat_results"][c], errors="coerce")

data['sat_results']['sat_score'] = data['sat_results'][cols[0]] + data['sat_results'][cols[1]] + data['sat_results'][cols[2]]

def find_lat(loc):
    coords = re.findall("\(.+, .+\)", loc)
    lat = coords[0].split(",")[0].replace("(", "")
    return lat

def find_lon(loc):
    coords = re.findall("\(.+, .+\)", loc)
    lon = coords[0].split(",")[1].replace(")", "").strip()
    return lon

data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(find_lat)
data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(find_lon)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors="coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors="coerce")


# # Condense datasets
class_size = data["class_size"]
class_size = class_size[class_size["GRADE "] == "09-12"]
class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"]

class_size = class_size.groupby("DBN").agg(numpy.mean)
class_size.reset_index(inplace=True)
data["class_size"] = class_size

data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]

data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]


# # Convert AP scores to numeric
cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

for col in cols:
    data["ap_2010"][col] = pd.to_numeric(data["ap_2010"][col], errors="coerce")


# # Combine the datasets
combined = data["sat_results"]

combined = combined.merge(data["ap_2010"], on="DBN", how="left")
combined = combined.merge(data["graduation"], on="DBN", how="left")

to_merge = ["class_size", "demographics", "survey", "hs_directory"]

for m in to_merge:
    combined = combined.merge(data[m], on="DBN", how="inner")

combined = combined.fillna(combined.mean())
combined = combined.fillna(0)

combined = combined.sort_values(by=["sat_score"])
#print(combined.columns)
abc = data["survey"].columns
#for i in abc:
#    plt.bar(numpy.arange(len(combined["sat_score"])),combined[i])
#    plt.xticks(numpy.arange(len(combined["sat_score"])),combined["sat_score"])
#    plt.title(i)
#    plt.show()
#N_s, N_t, Np seems showing correlation
    
#combined.plot.scatter(x="saf_s_11", y="sat_score")
#combined.plot.scatter(x="saf_t_11", y="sat_score")
#plt.show()
# majority of the sat_score gathered around 1200, some higher score for saf_t_!1 more than 7
# # Add a school district column for mapping
#print(combined.describe())
barlist = ["white_per", "asian_per", "black_per", "hispanic_per"]
for i in barlist:
    plt.bar(numpy.arange(len(combined["sat_score"])),combined[i])
    plt.xticks(numpy.arange(len(combined["sat_score"])),combined["sat_score"])
    plt.title(i)
    plt.show()
combined.plot.scatter(x="hispanic_per", y="sat_score")
# score is higher for high white_per, asian_per
# however some high asian_per seen for low score


def get_first_two_chars(dbn):
    return dbn[0:2]

combined["school_dist"] = combined["DBN"].apply(get_first_two_chars)


# # Find correlations
by_district = combined.groupby("school_dist").agg(numpy.mean)
by_district.reset_index(inplace=True)
#print(by_district.columns)
#m = Basemap(
#    projection='merc', 
#    llcrnrlat=40.496044, 
#    urcrnrlat=40.915256, 
#    llcrnrlon=-74.255735, 
#    urcrnrlon=-73.700272)
longtitude = by_district["lon"].tolist()
lattitude = by_district["lat"].tolist()
#m.scatter(longtitude, lattitude, s=20,latlon=True,zorder=2 )
#m.drawmapboundry()
#m.drawcoastlines()
#m.drawrivers()
correlations = combined.corr()
correlations = correlations["sat_score"]
#print(correlations)

# # Plotting survey correlations

# Remove DBN since it's a unique identifier, not a useful numerical value for correlation.
survey_fields.remove("DBN")

