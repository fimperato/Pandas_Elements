# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 2018

@author: Francesco

"""

import numpy as np
import pandas as pd

## Series 
## Vettore monodimensionale dati omogeneo, 
## strumento ottimale per memorizzare le osservazioni di una variabile
print("## Series ################")
my_series1 = pd.Series((1.1, 1.3, 1.5, 1.7, 1.9, 2.1, 2.1))
print(my_series1)
print(len(my_series1))
#### Series values
print("\r\n#### Series values")
print(my_series1.values)
print(type(my_series1.values))
#### Series index values
print("\r\n#### Series index values")
print(my_series1.index.values)
#### cambio l'ultimo valore
print("\r\n#### cambio l'ultimo valore")
my_series1[6] = 2.5
print(my_series1)
my_series1.values[-1] = 2.3
print(my_series1)

#### usiamo un anno come indice (passiamo un dizionario come costruttore)
print("\r\n#### anno come indice")
my_series2 = pd.Series({2015: 1.1, 2016: 1.3, 2017: 1.5})
print(my_series2)
#### creiamo la serie partendo da indici e valori, creati in precedenza
print("\r\n#### creiamo la serie partendo da indici e valori")
my_series3_index = pd.Index(range(2015,2018))
print(my_series3_index.values)
my_series3_values = list(range(20,23))
print(my_series3_values)

my_series3 = pd.Series(my_series3_values, index=my_series3_index)
print(my_series3)

my_series3.head() ## prime cinque righe di una serie
my_series3.tail() ## ultime cinque righe di una serie


## Dataframe  (frame di dati, tabella avente righe e colonne etichettate)
print("\r\n## Dataframe ################")
my_df1 = pd.DataFrame([
        (10, 20, 30),
        (11, 21, 31),
        (12, 22, 32)],
        columns=("col1", "col2", "col3"),
        index=("riga1", "riga2", "riga3")
        )
print(my_df1)
print("\r\n#### test on df")
print(my_df1["col1"].head())
print(my_df1["col2"].tail())
my_df1["col3"] = 100
print(my_df1)

#### Variazione indice
print("\r\n#### Variazione indice")
print(my_df1.index.values)
print(my_df1.columns.values)
my_df1 = my_df1.reset_index().set_index("col1")
print(my_df1)
print("10 (number) is index? " + str(10 in my_df1.index))

#### Variazioni dataframe
print("\r\n#### Variazioni dataframe")
my_df1 = my_df1.reset_index().set_index("index")
print(my_df1)

my_df2 = my_df1.reindex(my_df1.index, columns=my_df1.columns)
## aggiungo una colonna (valori di default NaN)
my_df2_columns = list(my_df1.columns) + ["col4"]
my_df2 = my_df1.reindex(my_df1.index, columns=my_df2_columns)
print(my_df2)

my_df2 = my_df1.reindex(my_df1.index, columns=my_df1.columns)
## aggiungo un index-riga
my_df2_index_1 = list(my_df1.index) + ["index_aggiunto"]
my_df2 = my_df1.reindex(my_df2_index_1 , columns=my_df2_columns)
print(my_df2)

## tolgo e aggiungo un indice-riga
my_df2_index_2 = [my_ind for my_ind in my_df1.index if my_ind[0]=='r'] + ["riga4"]
my_df2 = my_df1.reindex(my_df2_index_2, columns=my_df2_columns)
print(my_df2)

#### Pulizia dataframe
print("\r\n#### Pulizia dataframe")
my_df3 = my_df2.copy()
my_df3.dropna(how="all", inplace=True )
print(my_df3)
my_df3.dropna(how="all", axis=1, inplace=True )
print(my_df3)

#### Ricostruzione dati 
print("\r\n#### Ricostruzione dati ")
my_df4 = my_df2.copy()
righe_pulite4 = my_df4.notnull()
## righe sporche: my_df2[-righe_pulite2]
print("\r\n#### Ricostruzione dati (righe sporche -> a zero) ")
my_df4[-righe_pulite4] = 0 ## le righe sporche -> a zero
print(my_df4)

print("\r\n#### Ricostruzione dati (righe sporche -> media) ")
my_df4[-righe_pulite4] = np.nan
my_df4 = my_df4.fillna(my_df4.mean(axis=0)) ## le righe sporche -> pari alla media
print(my_df4)
#### Nota: my_df4.fillna(my_df4.mean(axis=1), axis=1) is not yet implemented
mean_on_row4 = my_df4.mean(axis=1)
for i, col in enumerate(my_df4):
    my_df4.iloc[:,i] = my_df4.iloc[:,i].fillna(mean_on_row4)
    
print(my_df4)

#### Map, Lambda 
print("\r\n#### Map, Lambda ")
my_df5 = my_df2.copy()
my_df5 = my_df5.reset_index()
transform_and_upper_case_index = my_df5["index"].map(lambda x : x[:5].upper()) 
print(transform_and_upper_case_index)