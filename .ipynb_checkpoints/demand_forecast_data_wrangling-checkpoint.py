#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:20:38 2020

@author: Ada
"""
runfile('demand_EDA.py')
# Store 1 item1 autocorrelation
store1 = train_df2[train_df2['store']==1]
store1_item1 = train_df2[(train_df2['store']==1) & (train_df2['item']==1)]
store1_item1 = store1_item1[['sales']]
plt.plot(store1_item1)
plt.show()

store1_item1_month = store1_item1.resample(rule='M').last()
plt.plot(store1_item1_bymonth)
plt.show()
store1_item1_month_diff = store1_item1_month.diff()
store1_item1_month_autocorr = store1_item1_month_diff['sales'].autocorr()
print("The autocorrelation of monthly sales changes is %4.2f" 
      %(store1_item1_month_autocorr))

index_month = store1_item1.index.month
store1_item1_month_mean = store1_item1.groupby(index_month).mean()
plt.plot(store1_item1_month_mean)
plt.show()

store1_item1_year = store1_item1.resample(rule='A').last()
plt.plot(store1_item1_year)
plt.show()

##Autocorrelation function (acf)
# Import the acf module and the plot_acf module from statsmodels
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

# Compute the acf array of store1_item1_month
acf_array = acf(store1_item1_month)
print(acf_array)

# Plot the acf function
plot_acf(store1_item1_month, alpha=1)
plt.show()
