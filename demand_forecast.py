#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:11:15 2020

@author: Ada
"""
import pandas as pd
import matplotlib.pyplot as plt

filename = 'train.csv'
train_df = pd.read_csv (filename)
print(train_df.head())
print(train_df.tail())
print(train_df.dtypes)
print(train_df.isnull().sum())
train_df = train_df.set_index('date')

train_df.index = pd.to_datetime(train_df.index)
plt.style.use('fivethirtyeight')
train_subset = train_df['2013-01':'2013-06']
ax = train_subset['sales'].plot()
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
ax.set_title('Sales of all 10 stores all items')
plt.show()

#Sample plot of store 1 item 1
store1_df = train_df[train_df['store']==1]
store1_item1 = store1_df[store1_df['item']==1]
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

