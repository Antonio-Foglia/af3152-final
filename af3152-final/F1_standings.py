#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:13:55 2020

@author: antoniofoglia
"""
import requests
import bs4
import pandas as pd


def f1(year):
    html=standings(year)
    with open("templates/F1_years/F1_{}.html".format(year),"w") as file:
        file.write(html)
    return

def standings(year):
    bs=bs4.BeautifulSoup(requests.get('https://www.formula1.com/en/results.html/{}/team.html'.format(year)).content,'lxml')
    tables=bs.find_all('table')
    try:
        df=pd.read_html(str(tables[0]))[0]
    except IndexError:
        return '<p> This is not a valid year!! <b>Please return to the previous page.</b> </p>'
    df.drop(['Unnamed: 0','Unnamed: 4'], axis=1, inplace=True)
    html=df.to_html()
    return html
    
    

