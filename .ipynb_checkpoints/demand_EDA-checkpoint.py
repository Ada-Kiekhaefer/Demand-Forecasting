#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:11:15 2020

@author: Ada
"""
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

#import training data
filename = 'train.csv'
train_df_raw = pd.read_csv(filename)
print(train_df_raw.head())
print(train_df_raw.tail())
print(train_df_raw.dtypes)
print(train_df_raw.isnull().sum())
train_df = train_df_raw.copy()
train_df = train_df.set_index('date')
train_df.index = pd.to_datetime(train_df.index)
plt.style.use('fivethirtyeight')
train_subset = train_df['2013-01':'2013-06']
ax = train_subset['sales'].plot()
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
ax.set_title('Sales of all 10 stores all items in 2013')
plt.show()

#Sample plot of store 1 item 1
#store1_df = train_df[train_df['store']==1]
#store1_item1 = store1_df[store1_df['item']==1]
store1_item1 = train_df[(train_df.store==1) & (train_df.item==1)]
ax1 = store1_item1['sales'].plot()
ax1.set_xlabel('Date')
ax1.set_ylabel('Sales')
ax1.set_title('Sales of store 1 item 1')
plt.show()

#Moving average plot of store1 item1
store1_item1_mean = store1_item1.rolling(window=7).mean()
ax2 = store1_item1_mean['sales'].plot()
ax2.set_xlabel('Date')
ax2.set_ylabel('Sales')
ax2.set_title('Weekly rolling mean of sales of store 1 item 1')
plt.show()

#Aggregation plot
index_month = store1_item1.index.month
store1_item1_bymonth = store1_item1.groupby(index_month).mean()
ax3 = store1_item1_bymonth['sales'].plot()
ax3.set_xlabel('Date')
ax3.set_ylabel('Sales')
ax3.set_title('Monthly average sales of store 1 item 1')
plt.show()

#summarizing data max,mean,sum of each item at each store
items_mean = train_df.groupby(['store','item']).mean()
#items_mean = train_df.groupby(['store','item'])['sales'].mean()
items_max = train_df.groupby(['store','item']).max()
items_max_sum = train_df.groupby(['store','item']).agg(['max','sum'])
items_max_mean_sum = train_df.groupby(['store','item']).agg(['max','mean','sum'])

#accessing data
print(items_mean)
print(items_mean.loc[1,:]) #store 1 all items
print(items_mean.loc[10,:]) #store 10 all items
print(items_mean.loc[1,1:10,:]) #store 1 item 1 to 10

#sum each items and each store
train_df2 = train_df_raw.copy()
train_df2['date'] = pd.to_datetime(train_df2['date'])
train_df2 = train_df2.set_index('date')
sum_all = train_df2['sales'].sum()
sum_items = train_df2.groupby('item')['sales'].sum()
plt.plot(sum_items)
plt.xlabel('Items')
plt.ylabel('Sales')
plt.title('Sum of each items at all stores')
plt.show()
sum_stores = train_df2.groupby('store')['sales'].sum()
plt.plot(sum_stores)
plt.xlabel('Stores')
plt.ylabel('Sales')
plt.title('Sum of all items at each stores')
plt.show()

