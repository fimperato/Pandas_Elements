# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 2018

@author: Francesco

"""

# ELABORAZIONE DATI CSV

import pandas as pd
#import xlrd

DF1 = pd.read_excel("Domini_min.xlsx")

## print the column names
print(DF1.columns)

EXCEL_FILE = pd.ExcelFile("Domini_min.xlsx")
SHEET_NAMES = EXCEL_FILE.sheet_names
print(SHEET_NAMES[1])
DF2 = EXCEL_FILE.parse(SHEET_NAMES[1])
print(DF2)

print("\r\nCiclo tutti gli sheet")
for SHEET_ITEM in SHEET_NAMES:
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
    DF_SHEET_ITEM.set_index(['cod_dominio', 'codice'], inplace=True)
    print(DF_SHEET_ITEM)
