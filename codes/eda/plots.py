#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:44:18 2020

@author: Ada
"""
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


def plot_store_item(df, store = 1, item = 1):
    store_item = df[(df.store == store) & (df.item == item)]
    ax1 = store_item['sales'].plot()
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Sales')
    ax1.set_title(f'Sales of store {store} item {item}')
    plt.show()

def plot_timeseries_subset(df, t_start = '2013-01', t_end = '2017-12'):
    train_subset = df[t_start:t_end]
    ax = train_subset['sales'].plot()
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales of all 10 stores all items')
    plt.show()

def plot_weekly_average(df, store = 1, item = 1):
    store_item = df[(df.store == store) & (df.item == item)]
    store_item_mean = store_item.rolling(window=7).mean()
    ax = store_item_mean['sales'].plot()
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title(f'Weekly rolling mean of sales of store {store} item {item}')
    plt.show()    

def plot_monthly_average(df, store = 1, item = 1):
    store_item = df[(df.store == store) & (df.item == item)]
    index_month = store_item.index.month
    store_item_bymonth = store_item.groupby(index_month).mean()
    ax = store_item_bymonth['sales'].plot()
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title(f'Monthly average sales of store {store} item {store}')
    plt.show()
   