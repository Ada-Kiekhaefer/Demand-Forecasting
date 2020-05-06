#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:44:18 2020

@author: Ada
"""
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

def df_subset(df, store = 1, item = 1, t_start = '2013-01', t_end = '2017-12'):
    """ A function to subset dataframe 
    
    Return a dataframe of specific item at a specific store and time period
    
    :param df: dataframe of stores sales
    :param store: a store number
    :param item: product item number
    :param t_start: start time
    :param t_end: end time
    
    >>> df_subset(df, store = 1, item = 1, t_start = '2013-01', t_end = '2013-12')
    
    """
    df_sub = df[(df.store == store) & (df.item == item)]
    df_sub = df_sub[t_start:t_end]
    return df_sub


def plot_store_item(df_sub):
    """ Time series plot of an item in a store 
    
    :param df_sub: dataframe of a store item sales
    
    >>> plot_store_item(df_sub)
    
    """
    
    ax1 = df_sub['sales'].plot()
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Sales')
    ax1.set_title('Sales of Store {} Item {}'
                  .format(df_sub['store'][0], df_sub['item'][0]))
    plt.show()


def plot_monthly_average(df_sub):
    df_sub_mean = df_sub.resample('M').mean()
    ax = df_sub_mean['sales'].plot()
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Monthly average sales of store {} item {}'
                 .format(int(df_sub_mean['store'][0]),
                 int(df_sub_mean['item'][0])))
    plt.show()  
    

def plot_monthly_variation(df_sub):
    index_month = df_sub.index.month
    df_sub_by_month = df_sub.groupby(index_month).mean()
    ax = df_sub_by_month['sales'].plot()
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Monthly average sales of store {} item {}'
                 .format(int(df_sub_by_month['store'][1]),
                 int(df_sub_by_month['item'][1])))
    plt.show()


def summary_stats(df_sub):
    items_stats = df_sub['sales'].agg(['max','mean','sum'])
    print('Store {} Item {} summary statistics:'
          .format(df_sub['store'][0], df_sub['item'][0]))
    print(items_stats)
    return items_stats


def df_subset_monthly_mean(df_sub):
    store_item_monthly_mean = df_sub.resample('M').mean()
    return store_item_monthly_mean
    

































  