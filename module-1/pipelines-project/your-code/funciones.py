#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd

def select_year(): 
    return int(input('Introduce el año que quieres analizar: '))

def rename_columns(dfshark): 
    ''' Renombramos columnas para que no den errores '''    
    res = dfshark.rename(columns={'Sex ':'Sex', 
                        'Species ':'Species', 
                        'Case Number': 'Case_Number',                               
                        'Fatal (Y/N)': 'Fatal',                                 
                        'Investigator or Source': 'Source',                                 
                        'href formula': 'href_formula', 
                        'Case Number.1': 'Case_1', 
                        'Case Number.2': 'Case_2', 
                        'original order': 'order', 
                        'Unnamed: 22': 'Unnamed_22', 
                        'Unnamed: 23': 'Unnamed_23'
                       })

    return res



def remove_cols(dfrc): 
    ''' 
    Eliminamos las columnas que tienen vacios más de la mitad de sus registros. 
    Eliminamos columnas que no nos servirán en el análisis. 
    '''
    res = dfrc[['Year', 'Type', 'Country', 'Area', 'Activity', 'Injury', 'Fatal']]        
    return res

def remove_nan_rows(dfrr): 
    return dfrr.dropna()