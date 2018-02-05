# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 2018

@author: Francesco

"""

import numpy as np
import pandas as pd
import matplotlib, matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split

## Dati grezzi da csv
## GSPC: prezzi di chiusura di Standard&Poor 500
DF_TOTAL_DATA = pd.read_csv("dataset/gspc/GSPC_by_yahooFinance.csv").set_index("Date")
print("# Get the data")
print("## index dei data: ")
print(DF_TOTAL_DATA.index)

#### Seleziono un sottoinsieme di dati da usare come dataset 
#### per il test di regressione
DF_TOTAL_DATA.index = pd.to_datetime(DF_TOTAL_DATA.index)
print("## condition, selezione index: ")
print(DF_TOTAL_DATA.index > pd.to_datetime('2010-01-01'))
DF_DATASET = DF_TOTAL_DATA.iloc[DF_TOTAL_DATA.index > pd.to_datetime('2010-01-01')] 


## Splitting di training e test set
print("## Splitting TRAINING and TEST set")
DF_train, DF_test = train_test_split(DF_DATASET, test_size=0.2)
print("#### training set (dopo split): ")
print(DF_train.head())
print("#### shape DF_DATASET: ")
print(DF_DATASET.shape)
print("#### shape DF_train: ")
print(DF_train.shape)
print("#### shape DF_test: ")
print(DF_test.shape)

print("#### variabile dominio: ")
print("#### shape DF_DATASET.index: ")
print(DF_DATASET.index.shape)

print("#### Order DF_train by index (for subtract): ")
DF_DIFF1 = DF_DATASET.subtract(DF_train) 
DF_train.sort_index(inplace=True)
DF_test.sort_index(inplace=True)
print(DF_train.head())
#Can only compare them if identically-labeled DataFrame objects (i.e. when test_size=0):
#DF_DIFF1 = DF_DATASET != DF_train 
print("#### DIFF of DF: ")
print(DF_DIFF1.head())

## Preparo il modello ed eseguo il fit sui dati di test
print("## TRAIN: Prepare the model and fit it ")
olm = lm.LinearRegression()
X_train = np.array([x.toordinal() for x in DF_train.index])[:, np.newaxis]
print("#### shape X (dominio): ")
print(X_train.shape)

y = DF_DATASET['Close']
y_train = DF_train['Close']
olm.fit(X_train, y_train)

print("#### DIFF of Y of DF: ")
Y_DIFF1 = y.subtract(y_train)
print(Y_DIFF1.head())
## verifica tramite csv esportato:
#DF_DATASET.to_csv("DF_DATASET.csv", sep=',', encoding='utf-8')
#DF_train.to_csv("DF_train.csv", sep=',', encoding='utf-8')

## Predizione dei valori:
print("## PREDIZIONE su dati di train stessi (prova)")
yp_on_train = [olm.predict(x.toordinal())[0] for x in DF_train.index]
#### Valutazione-prova del modello (con lo stesso train set!)
olm_score = olm.score(X_train, yp_on_train)
print("## SCORE del modello usato (prova): "+str(olm_score))
      
print("## PREDIZIONE su dati di test ")
X_test = np.array([x.toordinal() for x in DF_test.index])[:, np.newaxis]
print("#### shape X (dominio di TEST): ")
print(X_test.shape)
y_test = DF_test['Close']
print("#### shape Y (variabile dipendente di TEST): ")
print(y_test.shape)

yp_on_test = [olm.predict(x.toordinal())[0] for x in DF_test.index]
#### Valutazione del modello (con lo stesso train set)
olm_score = olm.score(X_test, y_test)
print("## SCORE del modello usato (TEST): "+str(olm_score))
      
## Plot:
matplotlib.style.use("ggplot")

#### Plot di entrambi i set di valori (verifico y_test rispetto ai y predetti su X_test)
plt.plot(DF_test.index, y_test)
plt.plot(DF_test.index, yp_on_test)

plt.title("OLS Regression")
plt.xlabel("Anno")
plt.ylabel("S&P 500 (chiusure)")
plt.legend(["Reale", "Predetto"], loc="lower right")

plt.savefig("my_plot_img/valoriChiusuraSP-regressioneLineare.pdf")
