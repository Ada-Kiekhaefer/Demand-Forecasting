#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:56:42 2020

@author: Ada
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARMA
#from eda.utils import *
import eda
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

filename = '../data/train.csv'
df = pd.read_csv(filename)
print('Shape of data frame {}'.format(df.shape))
print(df.head())

df = df.set_index('date')
df.index = pd.to_datetime(df.index)

store = 2
item = 2
t_start='2014-01'
t_end='2014-12'

df_sub = eda.df_subset(df, store=2, item=2, t_start='2014-01', t_end='2017-12')

eda.plot_store_item(df_sub)

eda.plot_monthly_average(df_sub)

store_item_stat = eda.summary_stats(df_sub)

df_sub_monthly_mean = eda.df_subset_monthly_mean(df_sub)

# Plot the autocorrelation
plot_acf(df_sub_monthly_mean['sales'], alpha = 1, lags=12)
plt.show()

#Fit AR model
mod = ARMA(df_sub_monthly_mean['sales'], order = (10,0))
result = mod.fit()
print(result.summary())
print(result.params)

#Forecasting
result.plot_predict(start = '2018-01-31', end = '2018-12-31')
plt.show()

# plot partial ACF (PACF)
plot_pacf(df_sub_monthly_mean['sales'], alpha = 1, lags=20)
plt.show()

# get Akaike  information creteria (AIC) and Bayesian information creteria (BIC)
print(result.aic)
print(result.bic)

# MA model
mod = ARMA(df_sub_monthly_mean['sales'], order = (0,10)) # reverse order with AR model
result = mod.fit()
print(result.summary())
print(result.params)
result.plot_predict(start = '2018-01-31', end = '2018-12-31')
plt.show()

