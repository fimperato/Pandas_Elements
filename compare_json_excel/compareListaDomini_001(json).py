# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 

@author: Francesco
"""

import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import json
from pprint import pprint
from cytoolz.dicttoolz import merge
#import flatten_json as flatten_json

## JSON Import
print("\r\nJSON Import")
data = json.load(open('json\Domini_min_02.json'))
pprint(data)

## Case 1.1
print("\r\nJSON Import -> to DF [1.1]")
NORMALIZED_DATA_DOMINI = json_normalize(data['listaDomini'])
df_by_json1 = pd.DataFrame.from_dict(NORMALIZED_DATA_DOMINI, orient='columns')
print(df_by_json1.head())

## Case 1.2
print("\r\nJSON Import -> to DF [1.2]")
NORMALIZED_DATA_DOMINI2 = json_normalize(data['listaDomini'], record_path='domini')
df_by_json2 = pd.DataFrame.from_dict(NORMALIZED_DATA_DOMINI2, orient='columns')
print(df_by_json2.head())

## Case 1.3
# ref. https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

print("\r\nJSON Import -> to DF (flatten) [1.3]")
NORMALIZED_DATA_DOMINI3 = json_normalize(data['listaDomini'])
FLAT_DATA_DOMINI3 = flatten_json(data['listaDomini'][0])
print(FLAT_DATA_DOMINI3)

## Case 1.4
print("\r\nJSON Import -> to DF [1.4]")
lista_domini = data['listaDomini']
NORMALIZED_DATA_DOMINI4 = json_normalize(lista_domini, 'codice') # not used
## read_json accetta array di uguale lunghezza (Domini_min_02.json ha array vuoti finali)
df_read4 = pd.read_json('json\Domini_min.json')
print(df_read4.listaDomini.values.tolist())

'''
def flattenColumn(input, column):
    column_flat = pd.DataFrame([[i, c_flattened] for i, y in input[column].apply(list).iteritems() for c_flattened in y], columns=['I', column])
    column_flat = column_flat.set_index('I')
    return input.drop(column, 1).merge(column_flat, left_index=True, right_index=True)
'''

## Case 1.5
print("\r\nJSON Import -> to DF [1.5]")
#df_read5 = pd.read_json('json\LetturaDominiService.json', grab_nest=('listaDomini','domini')) 
with open('json\Domini_min_02.json') as fDomini:
    data5 = json.load(fDomini)
    
df_by_json5 = pd.DataFrame(data5['listaDomini'])
print(df_by_json5)

## Case 1.6
print("\r\nJSON Import -> to DF [1.6]")
from pandas.io.json import json_normalize
with open('json\Domini_min_02.json') as fDomini:
    data6 = json.load(fDomini)
# Loading the json string into a structure
listaDomini6 = data6['listaDomini']
print(listaDomini6)

cnt = 0
for listaDominio6 in listaDomini6:
    cnt = cnt + 1
    print("\r\nJSON Import -> to DF [1.6.1]; iteration: "+str(cnt))
    df_expanded_temp = pd.concat([pd.DataFrame(listaDominio6), 
                              json_normalize(listaDominio6['domini'])], axis=1).drop('domini', 1)
    if cnt == 1:
        df_6 = df_expanded_temp
    else:
        df_6 = pd.concat([df_6, df_expanded_temp])
    #print(df_6)
    
## caso di cambio nome della prima colonna
#df_6 = df_6.rename(columns = {'codice':'new_name'})
## caso di rename tutte le colonne:
# df.columns = ['col1', 'col2', 'col3']
df_6.columns.values[0] = 'cod_dominio'
df_6.set_index(['cod_dominio', 'codice'], inplace=True)
print("\r\nDataframe select where (su colonne): ")
print(df_6.loc[(df_6['descrizione'] == 'REVOCATA')])
print("\r\nDataframe select where (su index): ")
df_6_1 = df_6.loc['STATO_CONFERMA']
print(df_6_1)
print("\r\nDataframe select where (su index-6_2): ")
df_6_2 = df_6.loc[['STATO_CONFERMA']]
print(df_6_2)
print("\r\nDataframe select where (su index-6_3 with query): ")
df_6_3 = df_6.query("cod_dominio == 'STATO_CONFERMA'")
print("\r\nDataframe select where (su multi-index-6_4 with query): ")
df_6_4 = df_6.query("cod_dominio == 'STATO_CONFERMA' and codice == '02'")
print(df_6_4)
print("\r\nDataframe select where (su multi-index-6_5): ")
df_6_5 = df_6.loc['STATO_CONFERMA','08']
print(df_6_5)

