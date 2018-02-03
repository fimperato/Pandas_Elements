# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:52:40 2018

@author: Francesco
"""

import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import json
from pprint import pprint

print("\r\nJSON Import -> to DF [1.0]")
with open('json\Domini_min.json') as fDomini:
    data_by_json = json.load(fDomini)
# Loading the json string into a structure

#json_dict6 = json.load(io.StringIO(data_by_json))
listaDomini_by_json = data_by_json['listaDomini']
print(listaDomini_by_json)

cnt = 0
for listaDominio_by_json in listaDomini_by_json:
    cnt = cnt + 1
    print("\r\nJSON Import -> to DF [1.1]; iteration: "+str(cnt))
    df_expanded_temp = pd.concat([pd.DataFrame(listaDominio_by_json), 
                              json_normalize(listaDominio_by_json['domini'])], axis=1).drop('domini', 1)
    if cnt == 1:
        df_lista_by_json = df_expanded_temp
    else:
        df_lista_by_json = pd.concat([df_lista_by_json, df_expanded_temp])
    #print(df_lista_by_json)
    
## cambio il nome della prima colonna
df_lista_by_json.columns.values[0] = 'cod_dominio'

#df_lista_by_json.set_index(['cod_dominio'], inplace=True)
#df_lista_by_json.sort_index(inplace=True)
print(df_lista_by_json)

## Excel Lista
print("\r\n## EXCEL Lista")
EXCEL_FILE = pd.ExcelFile("excel\Domini_min.xlsx")
SHEET_NAMES = EXCEL_FILE.sheet_names

cnt = 0
print("\r\nCiclo tutti gli sheet")
for SHEET_ITEM in SHEET_NAMES:
    cnt = cnt + 1
    SHEET_NAME = SHEET_ITEM.split(" - ")[0]
    print("SHEET_NAME: "+SHEET_NAME)
    DF_SHEET_ITEM = EXCEL_FILE.parse(SHEET_ITEM)
    ## cambio il nome della prima colonna
    DF_SHEET_ITEM.columns.values[0] = 'codice'
    DF_SHEET_ITEM.columns.values[1] = 'descrizione'
    DF_SHEET_ITEM['cod_dominio'] = SHEET_NAME
    # riordino le colonne dataframe:
    COLS = DF_SHEET_ITEM.columns.tolist()
    COLS = COLS[-1:] + COLS[:-1]
    #print(COLS)
    DF_SHEET_ITEM = DF_SHEET_ITEM[COLS]
    DF_SHEET_ITEM['codice'] = DF_SHEET_ITEM['codice'].astype(str)
    #DF_SHEET_ITEM.set_index(['cod_dominio'], inplace=True)
    if cnt == 1:
        df_lista_by_excel = DF_SHEET_ITEM
    else:
        df_lista_by_excel = pd.concat([df_lista_by_excel, DF_SHEET_ITEM])
        
## df_lista_by_excel finale
#df_lista_by_excel.sort_index(inplace=True)
print(df_lista_by_excel)

'''
DF_DIFF = df_lista_by_json.where(df_lista_by_json.values != df_lista_by_excel.values)
DF_DIFF = DF_DIFF[DF_DIFF['codice'].notnull() | DF_DIFF['descrizione'].notnull()]
print("\r\nDF_DIFF")
print(DF_DIFF)
'''

print("\r\n ## df_compare")
df_compare = df_lista_by_json.merge(df_lista_by_excel, how='outer', on=['cod_dominio'], suffixes=['_json', '_excel'])
df_compare['check'] = (df_compare.descrizione_json == df_compare.descrizione_excel) & (df_compare.codice_json == df_compare.codice_excel)
df_compare = df_compare[df_compare['check']==False]
#df_compare = df_compare.sort_values(['cod_dominio'], ascending=[True])
df_compare = df_compare.iloc[:,:-1]


## similarity 
from difflib import SequenceMatcher
import distance

def similar(a, b): 
    return SequenceMatcher(None, a, b).ratio()

df_compare['similarity_cod'] = 0
df_compare['similarity_cod'] = df_compare.apply(lambda row: similar(row.codice_json,row.codice_excel), axis=1)
#df_compare['Similarity'] = similar(""+str(df_compare.codice_json),""+str(df_compare.codice_excel))
#print( similar(df_compare.iloc[0].codice_json,df_compare.iloc[1].codice_excel) )
df_compare['similarity_desc'] = 0
df_compare['similarity_desc'] = df_compare.apply(lambda row: similar(row.descrizione_json,row.descrizione_excel), axis=1)

df_compare = df_compare[(df_compare['similarity_cod']>0.60) | (df_compare['similarity_desc']>0.60)]
df_compare = df_compare.sort_values(['cod_dominio', 'codice_json', 'descrizione_json'], ascending=[True, True, True])
df_compare = df_compare.iloc[:,:-2]

print(df_compare)