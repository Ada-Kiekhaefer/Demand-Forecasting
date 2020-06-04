#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:54:37 2020

@author: Ada
"""
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

model_param1 = 0.5
model_param2 = 100

def df_subset_monthly_mean(df_sub):
    store_item_monthly_mean = df_sub.resample('M').mean()
    return store_item_monthly_mean