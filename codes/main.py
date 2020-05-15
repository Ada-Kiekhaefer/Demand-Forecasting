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
#from eda.utils import *
import eda
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error

filename = '../data/train.csv'
#df = pd.read_csv(filename)
df = pd.read_csv(filename, index_col='date', parse_dates=True)
print('Shape of data frame {}'.format(df.shape))
print(df.head())

# df = df.set_index('date')
# df.index = pd.to_datetime(df.index)

#Statistics by group


#Subsetting data
df_sub = eda.df_subset(df, store=2, item=2, t_start='2014-01', t_end='2017-12')

#Plotting data
eda.plot_store_item(df_sub)
eda.plot_monthly_average(df_sub)
store_item_stat = eda.summary_stats(df_sub)

#Monthly average
df_sub_monthly_mean = eda.df_subset_monthly_mean(df_sub)

# Plot the autocorrelation
plot_acf(df_sub_monthly_mean['sales'], alpha = 1, lags=12)

#Integrated of order 1, denoted by parametemer d in ARIMA model
df_diff = df_sub_monthly_mean.diff(periods=1).dropna()
df_diff['sales'].plot()
plot_acf(df_diff['sales'])

#Split train/test
train = df_sub_monthly_mean['sales']

#Fit AR model
mod = ARIMA(train, order = (10,0,0))
result = mod.fit()
print(result.summary())
print(result.params)

#Forecasting
result.plot_predict(start = '2018-01-31', end = '2018-12-31')

# plot partial ACF (PACF)
plot_pacf(df_sub_monthly_mean['sales'], alpha = 1, lags=12)

# get Akaike  information creteria (AIC) and Bayesian information creteria (BIC)
print(result.aic)
print(result.bic)

# MA model
mod = ARIMA(train, order=(0,0,10)) # reverse order with AR model
result = mod.fit()
print(result.summary())
print(result.params)
result.plot_predict(start='2018-01-31', end='2018-12-31')
result_forecast = result.forecast(steps=12)[0]
plt.plot(result_forecast)

#ARIMA Model
model_arima = ARIMA(train, order=(9,1,0))
model_fit = model_arima.fit()
print(model_fit.aic)
#mean_squared_error(test, prediction)

#find smallest aic 

import itertools
import warnings
warnings.filterwarnings('ignore')


p = d = q = range(0, 5)
