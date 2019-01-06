# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:10:51 2018

@author: Siew Ling
for Data Quest Guided Project #3: Exploring Ebay Car Sales Data
"""

import numpy as np
import pandas as pd

autos = pd.read_csv("autos.csv", encoding="Latin-1")
#print(autos.head())
#print(autos.info())
"""
this data has 20 columns 5000rows
1. here are the columns with null data:
   vehicleType, gearbox, model, fuelType, notRepairDamage
2. [done] Column name needs changes

[Done]
Copy that array and make the following edits to columns names:
yearOfRegistration to registration_year
monthOfRegistration to registration_month
notRepairedDamage to unrepaired_damage
dateCreated to ad_created
The rest of the columnn names from camelcase to snakecase.
"""
#print(autos.columns) #print out columns name and change it accordingly
cols = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'abtest',
       'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model',
       'odometer', 'registration_month', 'fuel_type', 'brand',
       'unepaired_damage', 'ad_created', 'nr_of_pictures', 'postal_code',
       'last_seen']
autos.columns = cols
#print(autos.head())

"""
[done] price and odometer not in int type
ad_created time is 00:00:00
"""
desc = autos.describe(include='all')

"""
1. seller and offer_type hava same data across all rows
"""

autos["price"] = autos["price"].str.replace("$","").str.replace(",","").astype(int)
autos["odometer"] = autos["odometer"].str.replace("km","").str.replace(",","").astype(int)
autos.rename({"odometer":"odometer_km"},axis=1,inplace=True)
desc = autos.describe(include = 'all')
# check prince range for outlier
#print(autos["price"].unique().shape)
#print(autos["price"].describe())
#print(autos["price"].value_counts().head(5))
#print(autos["price"].value_counts().sort_index(ascending=True).tail(10))
#price_bool = autos["price"]> 100000
#xprice = autos.loc[price_bool,"price"]
#print(xprice.shape)

"""
1. 1421 cars listed as 0, changed to Nan
2. 53 car listed >100000, changed to Nan
"""
#print(autos["price"].describe(include='all'))
modprice_bool = (autos["price"] > 100000) | (autos["price"] == 0)
autos.loc[(modprice_bool),"price"] = np.nan
#print(autos["price"].describe(include='all'))
#print(autos["odometer_km"].unique().shape)
#print(autos["odometer_km"].describe())
#print(autos["odometer_km"].value_counts())
#print(autos["odometer_km"].value_counts().sort_index(ascending=True))

"""
1. 50 percentile of the car has odometer more than 150000km
"""
#print(autos["date_crawled"].value_counts(normalize=True,dropna=False))
#print(autos["date_crawled"].sort_index(ascending=True))
#print(autos["date_crawled"].str[0:10].value_counts().sort_index(ascending=True))
#print(autos["last_seen"].str[0:10].value_counts().sort_index(ascending=True))
#print(autos["ad_created"].str[0:10].value_counts().sort_index(ascending=True))
"""
very few add created before march 
date_crawled and last seen dates are within early march to early april
"""
#print(autos["registration_year"].value_counts().sort_index(ascending=True))
#print(autos["registration_year"].describe())
"""
[Done]found some outlier(>2016, <1900), removed
some registration month is zero
"""

goodyear_row = (autos["registration_year"]>=2016) | (autos["registration_year"] <=1900)
autos = autos.loc[~goodyear_row,:]
#print(autos.info())

#about brand
top_brand_value = autos["brand"].value_counts(normalize=True)
brand_list = autos["brand"].value_counts(normalize=True).index
#print(top_brand_value)
top_brand = []
for i in brand_list:
    #print(i, ":",top_brand_value[i])
    if top_brand_value[i] > 0.005:
        top_brand.append(i)
#print(top_brand)
mean_price_byBrand = {}
mean_mileage_byBrand ={}
for i in top_brand:
    mean_price = autos.loc[autos["brand"] == i,"price"].mean()
    mean_mileage = autos.loc[autos["brand"] == i,"odometer_km"].mean()
    mean_price_byBrand[i] = mean_price
    mean_mileage_byBrand[i] = mean_mileage
#print(mean_price_byBrand, mean_mileage_byBrand)
mean_price_Series = pd.Series(mean_price_byBrand,name="price")
mean_mileage_Series = pd.Series(mean_mileage_byBrand,name="mileage")
#mean_Dataframe = pd.concat([mean_price_Series,mean_mileage_Series],axis=1 )
#print(mean_Dataframe)
mean_DataFrame = pd.DataFrame(dict(price=mean_price_Series, mileage=mean_mileage_Series))
#print(mean_DataFrame[:5])
"""
3 most famous band
volkswagen 21% mean price: 6384
Opel 10% mean price: 5106
bmw 10% mean price:8250
mercedes 9% mean price:29511
audi 8% mean price:8965
"""
#for brand in top_brand:
#volkswagen = autos[autos["brand"] == "volkswagen"]
#vw_info = volkswagen.describe()
