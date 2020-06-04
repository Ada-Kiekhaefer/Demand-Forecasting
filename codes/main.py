#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:56:42 2020

@author: Ada
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import acf, pacf, adfuller
#from eda.utils import *
import eda
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error

filename = '../data/train.csv'
df = pd.read_csv(filename, index_col='date', parse_dates=True)
print('Shape of data frame {}'.format(df.shape))
print(df.head())

# df = df.set_index('date')
# df.index = pd.to_datetime(df.index)

#Statistics by store
stores_sum = df.groupby('store')['sales'].sum()
stores_stats = df.groupby('store')['sales'].describe()
stores_stats['mean'].plot()

#Statistics by items
items_stats = df.groupby('item')['sales'].describe()
items_stats['mean'].plot()

#Subsetting data
df_sub = eda.df_subset(df, store=2, item=2, t_start='2013-01', t_end='2017-12')

#test if data is stationary using Dicky-fuller test
result = adfuller(df_sub['sales'])
print(result)

#Plotting data
eda.plot_store_item(df_sub)
eda.plot_monthly_average(df_sub)
store_item_stat = eda.summary_stats(df_sub)

#Monthly average
df_sub_monthly_mean = eda.df_subset_monthly_mean(df_sub)

# Plot the autocorrelation
df_sub_monthly_mean['sales'].plot()
plot_acf(df_sub_monthly_mean['sales'], lags=24)
acf(df_sub_monthly_mean['sales'])

# plot partial ACF (PACF)
plot_pacf(df_sub_monthly_mean['sales'], lags=24)
pacf(df_sub_monthly_mean['sales'])

#test if data is stationary using Dicky-fuller test
result = adfuller(df_sub_monthly_mean['sales'])
print(result) 
#zero element is test statistics, the more negative means the more stationary
#second element is p-value
print('ADF statistics: ', result[0])
print('p-vlaue: ', result[1])

#Integrated of order 1, denoted by parametemer d in ARIMA model
df_diff1 = df_sub_monthly_mean.diff().dropna()
result = adfuller(df_diff1['sales'])
print(result)
fig, ax = plt.subplots()
df_diff1['sales'].plot(ax=ax)
plt.show()

#Integrated of order 2, denoted by parametemer d in ARIMA model
df_diff2 = df_sub_monthly_mean.diff().diff().dropna()
result = adfuller(df_diff2['sales'])
print(result)
fig, ax = plt.subplots()
df_diff2['sales'].plot(ax=ax)
plt.show()

#Split train/test
train = df_sub_monthly_mean.loc[:'2016', ['sales']]
test = df_sub_monthly_mean.loc['2017':, ['sales']]
fig,ax = plt.subplots()
train.plot(ax=ax)
test.plot(ax=ax)
plt.show()

#Fit AR model
model_ar = ARIMA(train, order = (10,0,0))
model_ar_fit = model_ar.fit()
print(model_ar_fit.summary())
#print(model_ar_fit.params)

#Forecasting
model_ar_fit.plot_predict(start = '2017-01-31', end = '2017-12-31')

# get Akaike  information creteria (AIC) and Bayesian information creteria (BIC)
print(model_ar_fit.aic)
print(model_ar_fit.bic)

# MA model
model_ma = ARIMA(train, order=(0,0,10)) # reverse order with AR model
model_ma_fit = model_ma.fit()
print(model_ma_fit.summary())
print(model_ma_fit.params)
model_ma_fit.plot_predict(start='2017-01-31', end='2017-12-31')
model_ma_forecast = model_ma_fit.forecast(steps=12)[0]
plt.plot(model_ma_forecast)
plt.show()

#ARIMA Model
#model parameters (p, d, q)
# p: a period taken for autoregressive (AR) model
# d: Integrated order, differencing (typically 1 or 2)
# period in moving average (MA) model
model_arima = ARIMA(train, order=(7,2,7)) #best aic 330 with pdq (7,2,7)
model_arima_fit = model_arima.fit()
print(model_arima_fit.aic)
#mean_squared_error(test, prediction)

eda.find_best_pdq(train, max_p=10, max_d=2, max_q=10)



