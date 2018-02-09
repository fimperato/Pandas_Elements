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

# http://pandas-docs.github.io/pandas-docs-travis/#returning-a-view-versus-a-copy
# false positive SettingWithCopyWarning 
#pd.options.mode.chained_assignment = None  # default='warn'

## Dati grezzi da csv (automobili data)
print("## Get the data")
DF_DATASET = pd.read_csv("dataset/automobile/imports-85.csv")
DF_DATASET.columns = ['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','wheel-base','length','width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']

print("## index dei data: ")
DF_DATASET.set_index("engine-size", inplace=True)
print(DF_DATASET.index)
print(DF_DATASET.head())

## pulizia dataset:
print("\r\n## pulizia dataset")
print(len(DF_DATASET.iloc[:,-1]))
prezzo_col = DF_DATASET.iloc[:,-1]
DF_DATASET.iloc[:,-1] = prezzo_col.map(lambda prezzo_i : np.nan if prezzo_i[:1]=='?' else prezzo_i[:])
DF_DATASET.dropna(inplace=True)
print(len(DF_DATASET.iloc[:,-1]))
DF_DATASET.iloc[:,-1] = DF_DATASET.iloc[:,-1].map(lambda prezzo_i : int(prezzo_i))

y = DF_DATASET.iloc[:,-1]
print(y.shape)

'''
y_list = [item for item in y if item!='?'] ## test
y = y.iloc[:].map(lambda x : np.nan if x[:1]=='?' else x[:])
y.dropna(inplace=True)
'''

## Splitting di training e test set
print("## Splitting TRAINING and TEST set")
DF_train, DF_test = train_test_split(DF_DATASET, test_size=0.2)

DF_train.sort_index(inplace=True)
DF_test.sort_index(inplace=True)
print("@ LOG DEBUG: "+str(DF_test._is_view))
print("@ LOG DEBUG: "+str(DF_test.is_copy))
DF_my_copy = DF_test.copy()
print("@ LOG DEBUG (DF_my_copy): "+str(DF_my_copy._is_view))
print("@ LOG DEBUG (DF_my_copy): "+str(DF_my_copy.is_copy))

## Preparo il modello ed eseguo il fit sui dati di test
print("## TRAIN: Prepare the model and fit it ")
olm = lm.LinearRegression()
X_train = np.array(DF_train.index)[:, np.newaxis]
print("#### shape X (dominio): ")
print(X_train.shape)
y_train = DF_train.iloc[:,-1] # 'price'
print(y_train.shape)
olm.fit(X_train, y_train)

## Predizione dei valori:
print("## PREDIZIONE su dati di train stessi (prova)")
yp_on_train = [olm.predict(x) for x in DF_train.index]
#### Valutazione-prova del modello (con lo stesso train set!)
olm_score = olm.score(X_train, yp_on_train)
print("## SCORE del modello usato (prova): "+str(olm_score))
# result: 1.0
      
print("## PREDIZIONE su dati di test ")
X_test = np.array(DF_test.index)[:, np.newaxis]
print("#### shape X (dominio di TEST): ")
print(X_test.shape)
y_test = DF_test['price']
print("#### shape Y (variabile dipendente di TEST): ")
print(y_test.shape)

yp_on_test = [olm.predict(x) for x in DF_test.index]
#### Valutazione del modello (con lo stesso train set)
olm_score = olm.score(X_test, y_test)
print("## SCORE del modello usato (TEST): "+str(olm_score))


## Plot:
matplotlib.style.use("ggplot")
#### Plot di entrambi i set di valori (verifico y_test rispetto ai y predetti su X_test)
plt.plot(DF_test.index, y_test)
plt.plot(DF_test.index, yp_on_test)
plt.title("OLS Regression")
plt.xlabel("Engine-size")
plt.ylabel("Prezzo")
plt.legend(["Reale", "Predetto"], loc="lower right")

'''
print("\r\nCHECK")
print(DF_test.index)
print(olm.predict(DF_test.index[-1]))
'''

#### export plot
plt.savefig("my_plot_img/automobiliPrice-regressioneLineare.pdf")
