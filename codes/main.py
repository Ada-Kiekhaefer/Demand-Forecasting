#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:56:42 2020

@author: Ada
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from eda.utils import *

filename = '../data/train.csv'
train_df_raw = pd.read_csv(filename)
print(train_df_raw.shape)
print(train_df_raw.dtypes)
print(train_df_raw.head())
print(train_df_raw.tail())

train_df = train_df_raw.copy()
train_df = train_df.set_index('date')
train_df.index = pd.to_datetime(train_df.index)
plot_timeseries_subset(train_df, t_start = '2013-01', t_end = '2017-12')

plot_store_item(train_df, store = 1, item = 10)

plot_monthly_average(train_df, store = 1, item = 1)

plot_monthly_variation(train_df, store = 1, item = 20)

store_item_stat = summary_stats(train_df, store = 1, item = 1)

